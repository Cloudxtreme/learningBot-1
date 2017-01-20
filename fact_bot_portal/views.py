from django.shortcuts import render
from .models import Fact
# Create your views here.
def fact_show(request):
    facts = Fact.objects.all()
    return render(request, 'fact_bot_portal/fact_show.html', {'facts': facts})

