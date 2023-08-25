from django.urls import path, include
import apis.views as api_view
from django.contrib import admin
from apis import views
from django.urls import resolve
"""
result = resolve('/base/url/1/')  # Replace with your actual URL
print(result)
"""
urlpatterns = [
  #  path('details/', api_view.DetailView.as_view()),
   # path('attendance/', api_view.AttendanceView.as_view()),
    #path('marks/', api_view.MarksView.as_view()),
    #path('timetable/', api_view.TimetableView.as_view()),
    
    path('<int:dept_id>/', api_view.BatchListByDept.as_view(), name='batch-list-by-dept'),
]
