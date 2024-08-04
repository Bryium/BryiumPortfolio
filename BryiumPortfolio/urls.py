from django.contrib import admin
from django.urls import path, include

from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', include('Home.urls')),
    path('Home/<str:email>/', views.home, name='home_with_email'),
]

