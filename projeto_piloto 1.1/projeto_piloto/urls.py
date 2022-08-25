from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('data_visualizer.urls')),
    path('admin/', admin.site.urls),
]