from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<slug:slug_room>/', views.room_detail, name='room_detail'),
    path('rooms/<slug:slug_room>/book-application/', views.book_application, name='book_application'),
]

urlpatterns += [
    path('hotel-admins/', views.admin_index, name='admin_index'),
    path('hotel-admins/add-room/', views.add_room, name='add_room'),
    path('hotel-admins/rooms/', views.admin_room_list, name='admin_room_list'),
    path('hotel-admins/book_applications/', views.admin_book_applications, name='admin_book_applications'),
    path('hotel-admins/book-applications/<slug:slug_book_application>/', views.admin_book_application_detail, name='admin_book_application_detail'),
]