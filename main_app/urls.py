from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.WishAdd.as_view(), name='add'),
    path('delete/<int:pk>', views.WishDelete.as_view(), name='wish_delete'),

]