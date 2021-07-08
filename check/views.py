from django.shortcuts import render, HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage 
from .models import *
import uuid
import requests
# Create your views here.
def home(request):
    return render(request, 'index.html')

def request(request):
    if request.POST:
        data = request.POST
        token = str(uuid.uuid4())
        Request(name = data['name'], 
        email = data['email'], 
        mobile = data['mobile'], 
        occupation = data['occupation'], 
        device_price = data['price'], 
        details = data['message'],
        token = token
        ).save()
        sendmail(request, data['name'], token, data['email'])
        # print(data['name'], "Saved")
        return render(request, 'success.html')
    else:
        return render(request, '404.html')

def sendmail(request, name, token, mail):
        ctx = {
            'user': name,
            'deny': token
        }
        message = get_template('mail.html').render(ctx)
        msg = EmailMessage(
            f'Request From {name}',
            message,
            'thakuriyatelecom@outlook.com',
            ['hackbypk@gmail.com'],
        )
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
        # print("Mail successfully sent")


def request_check(request, token):
    req = Request.objects.filter(token = token)[0]
    send_sms(req.name, req.mobile)
    return render(request, 'sent.html', {'name': req.name, 'mobile': req.mobile})

def send_sms(name, mobile):
    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"KUmNMjd6OaqT9JGYf0BCncp2gWuwIy1AFoZ3S7ebtQrHV4lkDETHWuwANvh8U4C5OrRQkq6txoy7sgp0",
    "message":f"Hello {name}, Sorry To Inform You That, You Are Not Eligible For Borrow From Thakuriya Telecom. You Have To Pay Full Amount At Once While Purchasing The Product.","language":"english","route":"q","numbers":mobile}
    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
