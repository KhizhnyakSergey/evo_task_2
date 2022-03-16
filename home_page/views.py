from mongoengine import DoesNotExist
from django.shortcuts import render
from home_page.forms import UserForm
from django.views import View
from home_page.models import User
from django.core.paginator import Paginator
# Create your views here.


class UserFormView(View):

    def get(self, request):
        user_form = UserForm()
        return render(request, 'home_page/register.html', context={'user_form': user_form})

    def post(self, request):
        user_form = UserForm(request.POST)
        email_add = None
        email_err = None
        email = request.POST['email']


        if user_form.is_valid():
            try:
                g = User.objects.filter(email__contains=email).all()
                if str(g.get()) == request.POST['email']:
                    email_err = request.POST['email']
                    # print('Уже виделись, ', email, email_err)
            except User.DoesNotExist:
                User.objects.create(**user_form.cleaned_data)
                email_add = request.POST['email']
                # print('Привет, ', email_add)
            
            # return HttpResponseRedirect('/')
        return render(request, 'home_page/register.html',
                        context={'user_form': user_form,
                                'email_add': email_add,
                                'email_err': email_err})


def check(request, page = 1):
    users = User.objects.order_by('-created')
    count_user = User.objects.count()
    paginator = Paginator(users, 10)
    users_paginator = paginator.page(page)
    return render(request, 'home_page/check.html',
                context={'users': users_paginator, 'count_user': count_user})
