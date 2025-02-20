from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):
    form = RegisterForm()

    messages.info(request=request, message='asas')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request=request, message="Usuario registrado")
            return redirect('contact:login')

    context = {
        'form': form,
    }
    return render(
        request=request,
        template_name='contact/register.html',
        context=context,
    )


@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        context = {
            'form': form,
        }

        return render(
            request=request,
            template_name='contact/register.html',
            context=context,
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    context = {
        'form': form,
    }

    if not form.is_valid():
        return render(
            request=request,
            template_name='contact/register.html',
            context=context,
        )

    form.save()
    return redirect('contact:user_update')


def login_view(request):

    form = AuthenticationForm(request=request)

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            messages.success(request=request, message='Login com sucesso')
            auth.login(request=request, user=user)
            return redirect('contact:index')
        messages.error(request=request, message='Erro no login')

    context = {
        'form': form
    }

    return render(
        request=request,
        template_name='contact/login.html',
        context=context,
    )

@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request=request)
    return redirect('contact:login')
