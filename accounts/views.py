from django.shortcuts import render, redirect
from django.views import View
from accounts.forms import UserRegistrations
import random
from utils import send_otp_code
from accounts.models import OtpCode
from django.contrib import messages


class UserRegisterView(View):
    form_class = UserRegistrations

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/register.html', {'from': form})

    def post(self, request):
        form = self.form_class(request.post)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'we sent you the code', 'success')
            return redirect('accounts:verify_code')
        return redirect('home:home')


class UserRegisterVerifyCodeView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
