from django.shortcuts import render
from django.views import View
from accounts.forms import UserRegistrations


class UserRegisterView(View):
    form_class = UserRegistrations

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/register.html', {'from': form})

    def post(self, request):
        pass
