from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
from django.core.exceptions import ValidationError


# Create your views here.

def index(request):
    # return HttpResponse('this is homepage')
    # messages.success(request, "testing")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse('this is aboutpage')
    return render(request, 'about.html')

def services(request):
    # return HttpResponse('this is servicepage')
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse('this is contactpage')

    if request.method == "POST" :
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        created_on = datetime.today()

        if not first_name or not last_name or not email:
            messages.warning(request, 'All fields are required.')
            return render(request, 'contact.html')

        if Contact.objects.filter(email=email).exists():
            messages.warning(request, 'Email already registered.')
            return render(request, 'contact.html')

        try:
            contact = Contact(first_name = first_name, last_name = last_name, email = email, mobile_no = mobile_no, created_on = created_on)
            contact.save()
            messages.success(request, "Your message has been sent")
            return redirect('contact')
        except ValidationError as e:
            messages.warning(request, f'Error creating : {e.messages[0]}')
            return redirect('contact')
            # return render(request, 'contact.html')
    
    return render(request, 'contact.html')
