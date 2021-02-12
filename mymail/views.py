from django.shortcuts import render
from django.core.mail import send_mail

def index(request):

    mymail_subject = 'Mail from '
    mymail_content = 'I am testing the sending of mail from django. Kya Haal hai Ji'
    mymail_from = 'tejinder3011@hotmail.com'
    mymail_to = ['mefehoj507@combcub.com']

    send_mail(mymail_subject + mymail_from, mymail_content, mymail_from, mymail_to,)

    return render(request, 'mymail/mailsent.html')

