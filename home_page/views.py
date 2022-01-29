from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from mongoengine import DoesNotExist
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
        email_add = None
        email_err = None
        email = request.POST['email']

        if user_form.is_valid():
            try:
                g = User.objects.filter(email__contains=email).all()
                if str(g.get()) == request.POST['email']:
                    email_err = request.POST['email']
                    print('Уже виделись, ', email, email_err)
            except User.DoesNotExist:
                User.objects.create(**user_form.cleaned_data)
                email_add = request.POST['email']
                print('Привет, ', email_add)
            except ObjectDoesNotExist:
                User.objects.create(**user_form.cleaned_data)
                email_add = request.POST['email']
                print('Привет, ', email_add)

            # return HttpResponseRedirect('/')
        return render(request, 'home_page/register.html',
                      context={'user_form': user_form,
                               'email_add': email_add,
                               'email_err': email_err})


def check(request):
    users = User.objects.all()[::-1]
    reverse_user = users[:15]
    count_user = User.objects.count()
    return render(request, 'home_page/check.html',
                  context={'users': users,
                           'count_user': count_user,
                           'reverse_user': reverse_user})

