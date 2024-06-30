from django.shortcuts import render,redirect
from django.core.mail import send_mail
from SendingMail import settings
from django.contrib import messages

# Create your views here.
def mail(request):
    if request.method=="POST":
        sndr=request.POST['em']
        sbj=request.POST['sb']
        mesg=request.POST['mg']
        user=settings.EMAIL_HOST_USER
        b=send_mail(sbj,mesg,user,[sndr])
        if b == 1:
            messages.success(request,"Mail sent Successfully")
            return redirect('/')
        else:
            messages.error(request,"Mail not Sent")
            return redirect('/')
    return render(request,'static/sendmail.html')
