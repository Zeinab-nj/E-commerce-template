from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('6265495830426A735A52584A46343468453331574F5979396C5A2B6339547A43564F61595555506C39556F3D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f' {code} کد تایید عضویت شما ',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
