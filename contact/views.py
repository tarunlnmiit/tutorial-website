from django.http import HttpResponse
from .models import Contact
# Create your views here.


def contact(request):
    '''Contact Function'''
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        if name and email and message:
            Contact(name=name, email=email, subject=subject, message=message).save()

    return HttpResponse('')