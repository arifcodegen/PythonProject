from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import users


def home(request):
    if request.method == 'POST':
        name = request.POST['username']
        pass1 = request.POST['password']

        # Use the custom manager's create_user method
        person = users.objects.create_user(name, password=pass1)

        # Save the user
        person.save()
        return HttpResponse("Sucessfully created")

    return render(request, 'login.html')
