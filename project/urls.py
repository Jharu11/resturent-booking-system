from django.urls import path
from .import views

urlpatterns = [
    path('', views.Profile, name="profile"),
    path('add-reservation/', views.AddReservation, name="add"),
    path('login/', views.Loginuser, name="Loginuser"),
    # url('register/', views.Register, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.LogoutView, name="logout"),
    path('view-reservations/',
        views.view_reservations, name="view_reservations"),
    path('update-reservation/<str:pk>/',
        views.UpdateReservation, name="update_reservation"),
]
