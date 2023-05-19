from django.shortcuts import render
from swan_page.models import Service, Contact, Team, Testimony
from datetime import datetime

# Create your views here.
def index(request):
    services = Service.objects.all()
    contacts = Contact.objects.all()
    teams = Team.objects.all()
    testimonys = Testimony.objects.all()

    now = datetime.now()
    current_year = now.strftime("%Y")


    context = {'current_year': current_year,
        'services':services,
        'contacts':contacts,
        'teams':teams,
        'testimonys':testimonys,
    }
    return render(request, 'swan_page/index.html', context)