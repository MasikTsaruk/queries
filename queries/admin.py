from django.contrib import admin
from .models import Query, QueryParameter, RequestLog

@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "uuid")

@admin.register(QueryParameter)
class QueryParameterAdmin(admin.ModelAdmin):
    pass

@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    pass