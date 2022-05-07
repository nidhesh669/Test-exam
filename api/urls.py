from django.urls import path
from .views import TodoAPIView,TodoAPIViews
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
        path('todo', TodoAPIView.as_view()),
        path('todo/<str:pk>', TodoAPIViews.as_view()) # to capture our ids
    ]