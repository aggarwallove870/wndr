from email import header
from hashlib import new
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Subscriber_newsletter,contact_us,DesktopMobileVideo
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse
from wsgiref.util import FileWrapper
# Create your views here.

def teams(request):
    return render(request,'teams.html')
# def start_page(request):

#     return render(request,'splash.html')

def home(request):
    video_obj=DesktopMobileVideo.objects.last()
    print(video_obj,"-----")
    if request.method == 'GET':
        return render(request, 'home.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email,"----->")
       
       
        match = Subscriber_newsletter.objects.filter(email__exact=email).exists()
        if match :
            print(match)
            response = {
                'is_taken': match
            }
            return JsonResponse(response)

      
        else:
            new_subscriber = Subscriber_newsletter(email=email)

            new_subscriber.save()
            subject ="Thankyou for subscribing"
            message = " You are successfully subscribed to our new updates"
            reply_to = ['info@wndr.com']
            from_email = "no-reply@wndr.website" #settings.EMAIL_HOST_USER
            subcriber_mail = EmailMessage(subject,message,"WNDR.com <do_not_reply@wndr.com>",[email],reply_to=reply_to)
            subcriber_mail.send(fail_silently=True)



            subject1 ="New Subscriber"
            recipients = ["info@wndr.com"]
            message1 = str(email) +" New user subscribed"
            adminmail = EmailMessage(subject1,message1,"WNDR.com <do_not_reply@wndr.com>",recipients,reply_to=reply_to)
            adminmail.send(fail_silently=True)

        return render(request, 'home.html',{"video_obj":video_obj})




def about(request):
    return render(request, 'roadmap.html')

def vision(request):
    return render(request, 'our-vision.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        review = request.POST.get('review')
        new_contact = contact_us(name=fname,email=email, address=address, phone=phone, review=review)
        new_contact.save()
        subject ="Contact Us"
        message = "Thank you for contacting us"
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [email])
        subject1 ="Contact Us Query"
        ctx = {
                'email': email,
                'fname':fname,
                'phone':phone,
                'address':address,
                'review':review
            }
        message1 =get_template('mail.html').render(ctx)
        send_mail(subject1, message1, email, [from_email])

    return render(request, 'contact.html')


def video_trailer(request):
    file = FileWrapper(open('video/WNDR TRAILER.mp4', 'rb'))
    response = HttpResponse(file, content_type='video/mp4')
    return response


def video_demo(request):
    file = FileWrapper(open('video/wndr_Tech demo (1080p).mp4', 'rb'))
    response = HttpResponse(file, content_type='video/mp4')
    return response

def video_url(request):
    videoobj=desktopVideo.objects.last()
    return render(request,"base.html",{"videoobj":videoobj})


def test(request):
    return render(request,"fetch.html")