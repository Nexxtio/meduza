from django.urls import path
from . import views
from .views import NotificationCreateView, NotificationDeleteView
# from users import views as user_views


urlpatterns = [
    path('', views.home, name='meduza-home'),
    path('notification/new/', NotificationCreateView.as_view(), name='notification-create'),
    path('notification/<int:pk>/delete/', NotificationDeleteView.as_view(), name='notification-delete'),
]
