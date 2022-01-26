from django.http import HttpResponseRedirect
from django.shortcuts import render
from home_page.forms import UserForm
from django.views import View
from home_page.models import User
# Create your views here.


class UserFormView(View):

    def get(self, request):
        user_form = UserForm()
        return render(request, 'home_page/register.html', context={'user_form': user_form})

    def post(self, request):
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            # совершаем какую-либо бизнес логику
            # к примеру сохранение в базу данных
            User.objects.create(**user_form.cleaned_data)
            # return HttpResponseRedirect('/')
        return render(request, 'home_page/register.html', context={'user_form': user_form})


def home(request):
    user_form = UserForm()
    users = User.objects.order_by('first_name')
    return render(request, 'home_page/home.html', context={'user_form': user_form, 'users': users})
