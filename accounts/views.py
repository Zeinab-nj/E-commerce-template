from django.shortcuts import render, redirect
from django.views import View
from accounts.forms import UserRegistrationsForm, VerifyCodeForm
import random
from utils import send_otp_code
from accounts.models import OtpCode
from django.contrib import messages
from .models import User


class UserRegisterView(View):
    form_class = UserRegistrationsForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/register.html', {'from': form})

    def post(self, request):
        form = self.form_class(request.POST)
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
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'],
                                         user_session['full_name'], user_session['password'])

                code_instance.delete()
                messages.success(request, 'you registered', 'success')
                return redirect('home:home')
            else:
                messages.error(request, 'your code is invalid', 'danger')
                return redirect('accounts:verify_code')
            return redirect('home:home')
