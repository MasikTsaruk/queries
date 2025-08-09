from django.contrib import admin
from .models import QueryUser

# Register your models here.
@admin.register(QueryUser)
class QueryUserAdmin(admin.ModelAdmin):
    pass