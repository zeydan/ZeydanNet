from django.shortcuts import render
from .models import Message

def contact(request):

    # get client ip address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    

    if request.method == "POST":
        fullname = request.POST['fullname']
        company = request.POST['company']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        ipaddress = ip

        send_message = Message.objects.create(fullname = fullname, company = company, email = email, subject = subject, message = message, ipaddress = ipaddress)
        send_message.save()
        return render(request, 'contact.html', {'pagetitle' : 'Contact', 'alert' : 'Thank you! Your message has been sent successfully.'})
    else:
        return render(request, 'contact.html', {'pagetitle' : 'Contact'})