from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from kavenegar import KavenegarAPI, APIException, HTTPException

from accounts.forms import UserAdminCreationForm
from accounts.helper import send_otp
from random import randint
from accounts.models import PhoneOTP, CustomUser


def signup(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('signup')
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
    if request.method == 'POST':
        phone = request.POST.get('phone')
        print(phone)
        password = request.POST.get('password')
        print(password)
        user = authenticate(phone=phone, password=password)
        print(user)

        if user is not None:
            login(request, user)
            otp = randint(1000, 9999)
            # send_otp(phone, otp)
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

    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
