from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
import apis.views as api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
    path('info/', include('info.urls')),
    path('api/department/', include('apis.urls')),

    path('api/bus/1/route/', api_view.UpRouteBusScheduleByDayView.as_view()),
    path('api/bus/2/route/', api_view.DownRouteBusScheduleByDayView.as_view()),
    path('api/bus/', api_view.RouteAll.as_view()),

    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(template_name='authentication/logout.html'), name='logout'),


    #__________________Django Toolbar________________
   # path("__debug__/", include("debug_toolbar.urls")), 
]
