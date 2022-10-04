from random import randint
from kavenegar import *
# from config.settings import KAVENEGAR_API


def send_otp(mobile, otp):
    try:
        print(mobile)
        api = KavenegarAPI('6B452B6E5070585972704F6C696D5A7A72766C67524D79496E4F6B6A59756463566B57696D65666E4636633D')
        params = {
            'sender': '10008663',
            'receptor': mobile,
            'message': f'your otp is {otp}'
        }
        response = api.sms_send(params)
        print(response)
        print(otp)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


def get_random_otp():
    return randint(10000, 99999)
