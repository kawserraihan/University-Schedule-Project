from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),

    path('teacher/<slug:teacher_id>/dashboard/',
         views.dashboard, name='dashboard'),

    path('teacher/<slug:teacher_id>/classes/', views.classes, name='classes'),
    path('teacher/<slug:teacher_id>/add_class_form/', views.add_class, name='add_class'),
    path('get_batches/', views.get_batches, name='get_batches'),
    path('get_sections/', views.get_sections, name='get_sections'),
    path('teacher/<slug:teacher_id>/classes/<int:class_id>/', views.view_class, name='view_class'),
    path('teacher/<slug:teacher_id>/classes/<int:class_id>/edit/', views.edit_class, name='edit_class'),
    path('teacher/<slug:teacher_id>/classes/<int:class_id>/delete/', views.delete_class, name='delete_class'),

]
admin.site.site_url = None
admin.site.site_header = 'My Site'
