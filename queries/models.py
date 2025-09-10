import uuid
from django.db import models
from accounts.models import QueryUser
from django.utils import timezone

class Query(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    recipient = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(QueryUser, on_delete=models.CASCADE, related_name="queries")

    template = models.TextField(help_text="Enter Here SQL query")
    db_dsn = models.TextField(help_text="Database DSN")

    last_executed_at = models.DateTimeField(null=True, blank=True)
    execution_count = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    password = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name


class QueryParameter(models.Model):
    PARAM_TYPES = [
        ('string', 'String'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('select', 'Select'),
        ('multiselect', 'MultiSelect'),
    ]

    name = models.CharField(max_length=255)  
    type = models.CharField(max_length=20, choices=PARAM_TYPES, blank=True)

    min_number = models.FloatField(blank=True, null=True)
    max_number = models.FloatField(blank=True, null=True)

    min_date = models.DateField(blank=True, null=True)
    max_date = models.DateField(blank=True, null=True)

    allowed_values = models.TextField(blank=True, null=True, help_text="Value1, Value2")

    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name='parameters')

    required = models.BooleanField(default=False)

    def multiselect_allowed_values(self):
        if self.allowed_values:
            return [select.strip() for select in self.allowed_values.split(',')]
        return []

    def __str__(self):
        return self.name

    

class RequestLog(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name='request_logs')
    request = models.TextField(help_text="SQL request")
    response = models.TextField(help_text="Ответ (result or error)", blank=True, null=True)
    response_code = models.PositiveIntegerField(help_text="response code(0 = success, 1 = error)", default=0)
    response_time = models.FloatField(help_text="time of execution", default=0.0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Log for query {self.query_id} at {self.created_at}"