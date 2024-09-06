
from django.contrib import admin
from django.urls import include,path
from first_app import views

urlpatterns = [
    path('', views.default_view, name='default_view'),
    path('admin/', admin.site.urls),
    path('first_app/',include('first_app.urls')),
    path('accounts/', include('allauth.urls')),
    path('upload', views.file_upload_view, name='file_upload_view'),
    path('accounts/profile/', views.home_view, name='home_view')
    


]
