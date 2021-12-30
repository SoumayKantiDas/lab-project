from django.contrib import admin
from django.urls import path, re_path
from Get_Code import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<str:user>/<str:name>/', views.commit_view, name='commit_view'),
    path('<str:user>/<str:name>/<str:ref>/', views.commit_files_view, name='commit_files_view'),
    path('<str:user>/<str:name>/<str:ref>/<str:file>/', views.code_view, name='code_view'),
]
