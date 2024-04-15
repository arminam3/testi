from django.urls import path

from .views import HomeView, theme_change_view, NotificationCreateView, search_users


urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('theme-change/', theme_change_view, name="theme_change"),
    path('search-users/', search_users, name="search_users"),
    path('notification-create/', NotificationCreateView.as_view(), name="notification_create"),
]