from django.core.mail import EmailMessage
import re
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib import messages

# Create your views here.


class HomeView(TemplateView):
    template_name = "home/home.html"

def mail_me(req):
    if req.method =='POST':
        name = req.POST['name']
        contact = req.POST['contact']
        msg = req.POST['msg']
        email = EmailMessage(
            'Someone Mailed',
            f"{name}:{contact}:{msg}",
            to=['arnab95gupta@gmail.com'],
        )
        try:
            email.send()
        except Exception as e:
            raise e
        else:
            messages.success(req,'Mail Sent!')
        return redirect("home:home")