from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery'),  # без 'gallery/'
    path('<int:image_id>/', views.image_detail, name='image_detail'),
]