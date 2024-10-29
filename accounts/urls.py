from django.urls import path
from accounts.views import UserRegisterView, UserRegisterVerifyCodeView, UserLoginView


app_name = 'accounts'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('verify/', UserRegisterVerifyCodeView.as_view(), name='verify_code'),
]
