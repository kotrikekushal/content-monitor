from django.urls import path
from . import views

urlpatterns = [
    path('keywords/', views.create_keyword),
    path('scan/', views.scan_content),
    path('flags/', views.get_flags),
    path('flags/<int:id>/', views.update_flag),
    path('', views.home),

]
