from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User
from second_app.forms import UserForm
# Create your views here.

def index(request):
    return HttpResponse("<em>Whatsupp</em>")

def helpview(request):
    help_dict = {"Help_tag": "This is the help template tag"}
    return render(request,'second_app/help.html', context=help_dict)

def formview(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return index(request)
    context = {'form': form}
    return render(request, 'second_app/users.html', context = context)

