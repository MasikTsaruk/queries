from django.urls import path
from . import views

urlpatterns = [
    path('create_query/', views.create_query, name='create'),
    path('create_query_parameter/<int:query_id>/', views.create_query_parameter, name='create_query_parameter'),
    path('queries_all/', views.queries_all, name='all'),
    path('queries_my/', views.queries_my, name='my'),
    path('delete_query/<uuid:query_uuid>', views.delete_query, name='delete'),
    path('edit_query/<uuid:query_uuid>', views.edit_query, name='edit'),
    path('run_query/<uuid:query_uuid>', views.run_query, name='run'),
    path('change_password/<uuid:query_uuid>', views.change_password, name='change'),
    path('reset/<uuid:query_uuid>', views.reset_password, name='reset'),
    path('run/<uuid:query_uuid>', views.run_query, name='run'),
    path('download_excel/<int:request_log_id>/', views.download_excel, name='download_excel'),
    path("queries/<uuid:query_uuid>/params/", views.manage_query_params, name="manage_query_params"),
    path("queries/params/<int:param_id>/delete/", views.delete_query_param, name="delete_query_param"),
]