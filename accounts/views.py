from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic, View
from kavenegar import KavenegarAPI, APIException, HTTPException
from django.contrib import messages
from random import randint
from accounts.models import PhoneOTP, CustomUser
from .forms import UserAdminCreationForm, LogInForm


def signup(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            phone = form.cleaned_data.get("phone")
            password = form.cleaned_data.get("password")
            user = CustomUser.objects.create_user(phone=phone, password=password)
            user.save()
        return redirect('verify')

        otp = randint(10000, 99999)
        try:
            print(phone)
            api = KavenegarAPI(
                '6B452B6E5070585972704F6C696D5A7A72766C67524D79496E4F6B6A59756463566B57696D65666E4636633D')
            params = {
                'sender': '10008663',
                'receptor': phone,
                'message': f'your otp is {otp}'
            }
            response = api.sms_send(params)
            print(response)
            print(otp)
        except APIException as e:
            print(e)
        except HTTPException as e:
            print(e)
        phone_otp = PhoneOTP.objects.create(phone=phone, otp=otp)
        return redirect('verify')

    return render(req, 'registration/signup.html', {'form': form})


def verify(request):
    if request.method == 'POST':
        user = request.user
        print(user)
        otp = request.POST.get('otp')
        custom_user = CustomUser.objects.get(phone=user)
        phone = custom_user.phone
        phone_otp = PhoneOTP.objects.filter(phone=phone, otp=otp)
        if phone_otp:
            return redirect('home')
        else:
            return redirect('login')
    print('hi')
    return render(request, 'registration/verify.html')


def login_view(request):
    form = LogInForm()
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            print(phone)
            password = form.cleaned_data.get('password')
            print(password)
            user = authenticate(phone=phone, password=password)
            print(user)
            if user is not None:
                login(request, user)
            # messages.success(request, 'شما با موفقیت وارد شدید!', 'error')
            return redirect('analyze_list')
        print(form.errors)
        # print(form.errors)
    # else:
    # messages.error(request, 'نام کاربری یا رمزعبور اشتباه است!', 'danger')

    return render(request, 'registration/login.html', {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'شما با موفقیت خارج شدید', 'success')
        return redirect('login')


# @login_required()
# def create_profile(request):
#     form = CreateProfileForm()
#     if request.method == 'POST':
#         form = CreateProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = CreateProfileForm()
#     else:
#         form = CreateProfileForm()
#     return render(request, 'profile.html', context={'form': form})


def forget_password(request):
    return render(request, 'registration/forget_password.html')
