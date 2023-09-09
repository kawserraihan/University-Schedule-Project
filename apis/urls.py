from django.urls import path, include
import apis.views as api_view
from django.contrib import admin
from apis import views
from django.urls import resolve

urlpatterns = [ 
    path('<int:dept_id>/batch', api_view.BatchListByDept.as_view(), name='batch-list-by-dept'),
    path('<int:dept_id>/batch/<int:batch_id>/section', api_view.SectionByDept.as_view()),
    path('<int:dept_id>/batch/<int:batch_id>/section/<int:section_id>/class', api_view.ClassDetailsByDayView.as_view()),
    path('', api_view.DepartmentAll.as_view()),
    
]
