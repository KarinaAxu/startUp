from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, ProfileForm, ForgotPasswordForm, ResetPasswordForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Profile, ResetPassword
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from datetime import timezone
from django.contrib.auth.models import User
import uuid

RESET_PASSWORD_TOKEN_EXPIRATION_PERIOD = 3600

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('/dishes/')
            form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_data = authenticate(request, username=user.username, password=form.cleaned_data.get('password'))
            if auth_data:
                auth_login(request, auth_data)
                return redirect('/dishes/')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('/auth/login/')

@login_required
def profile_page(request):
    profile, created = Profile.objects.get_or_create(owner=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('settings_page')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'user/settings.html', {'form': form, 'profile': profile})


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            token = uuid.uuid4()
            reset_password_entry, created = ResetPassword.objects.update_or_create(email=email, defaults={'token': token})
            email_template = loader.get_template('user/reset-password-mail.html')
            reset_link = f'http://localhost:8000/reset_password/{token}'
            email_content = email_template.render({'URL': reset_link, 'TOKEN': token})

            try:
                send_mail(
                    subject='Reset Your Password',
                    message='',
                    html_message=email_content,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False
                )
                return render(request, 'user/forgot-password.html', {'form': form, 'status': 'success'})
            except Exception as e:
                return render(request, 'user/forgot-password.html', {'form': form, 'status': 'failed', 'error': str(e)})
    else:
        form = ForgotPasswordForm()
    return render(request, 'user/forgot-password.html', {'form': form})

def reset_password(request, token):
    try:
        reset_password_entry = ResetPassword.objects.get(token=token)
        if (timezone.now() - reset_password_entry.created_at).total_seconds() > RESET_PASSWORD_TOKEN_EXPIRATION_PERIOD:
            reset_password_entry.delete()
            return render(request, 'user/reset-password.html', {'form': ResetPasswordForm(), 'message': 'Your link is expired, please try again!'})
    except ResetPassword.DoesNotExist:
        return render(request, 'user/reset-password.html', {'form': ResetPasswordForm(), 'message': 'Invalid or expired token!'})

    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.get(email=reset_password_entry.email)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            reset_password_entry.delete()
            return redirect('/auth/login/')
    else:
        form = ResetPasswordForm()

    return render(request, 'user/reset-password.html', {'form': form})