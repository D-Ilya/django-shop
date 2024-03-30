from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        if (form := UserLoginForm(data=request.POST)) and form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            if user := auth.authenticate(username=username, password=password):
                auth.login(request, user)
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form
    }

    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        if (form := UserRegistrationForm(
                data=request.POST
        )) and form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)

            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Регистрация',
        'form': form
    }

    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        if (form := ProfileForm(
                data=request.POST,
                instance=request.user,
                files=request.FILES
        )) and form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': 'Профиль',
        'form': form
    }

    return render(request, 'users/profile.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))
