from django.urls import path
from accounts.views import UserRegisterView


app_name = 'accounts'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
]
