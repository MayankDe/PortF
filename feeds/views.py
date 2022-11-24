from django.shortcuts import render
from .models import *

# Create your views here.


def home_page(request):
    myinfo = PersonalInformation.objects.all()
    myabout = About.objects.all()
    myskills = Projects.objects.all()
    skills = Skills.objects.all()
    context = {
        "info": myinfo,
        "about": myabout,
        "skills": myskills,
        "know": skills
    }

    return render(request, 'home_page.html', context)


def contact_view(request):
    if request.method == 'POST':
        
        full_name = request.POST['full_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        ct = Contact(full_name=full_name,email=email,subject= subject,message=message)
        messages.success(request,"Thanks for Contact!...")
        ct.save()
        
        
        try:
            send_mail(subject,message,email,[email])
            return render(request, 'contactapp/success.html')
        except BadHeaderError:
            HttpResponse('Invalid')

    return render(request, 'contactapp/contact.html')