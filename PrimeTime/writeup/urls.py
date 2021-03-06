from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.writeup_view),
    path('post-list/', views.postList, name='post-list'),
    path('post-detail/<str:pk>/', views.postDetail, name='post-detail'),
    path('post-create/', views.postCreate, name='post-create'),
    path('post-update/<str:pk>', views.postUpdate, name='post-update'),
    path('post-delete/<str:pk>', views.postDelete, name='post-update'),

]