from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Email
from .forms import EmailForm
from django.core.mail import send_mail
from Mysite301.settings import EMAIL_HOST_USER

import smtplib


def index(request):
    emails = Email.objects.all()
    return render(request, 'app10_1/index.html', {'emails': emails})


def compose(request):
    email_form = EmailForm()
    if request.method =='POST':
        email_form = EmailForm(request.POST)
        to = str(email_form['to'].value())
        subject = str(email_form['subject'].value())
        content = str(email_form['content'].value())
        send_mail(subject, content, EMAIL_HOST_USER, [to,], fail_silently=False)
        email = Email(to=to, subject=subject, content=content)
        email.save()
        # send_mymail()
        return HttpResponseRedirect('..')
    return render(request, 'app10_1/compose.html', {'form': email_form})


def send_mymail():
    fromaddr = 'info.karyal@gmail.com'
    toaddrs = 'sabinstha447@gmail.com'
    msg = 'Spam email Test'
    username = 'mail@gmail.com'
    password = 'pass@word'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

"""
Note:
- https://data-flair.training/blogs/django-send-email/
- https://blog.mailtrap.io/django-send-email/
- https://www.google.com/settings/security/lesssecureapps
- https://accounts.google.com/b/0/DisplayUnlockCaptcha
"""