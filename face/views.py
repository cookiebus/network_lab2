from django.shortcuts import render
from face.models import Person


# Create your views here.
def home(request):
    try:
        person = Person.objects.all()[0]
    except:
        person.name = "XXX"
        person.url = "yyy"

    return render(request, 'index.html', locals())

    
