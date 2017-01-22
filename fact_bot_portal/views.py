from django.shortcuts import render
from .models import Fact
from .forms import FactForm
from django.shortcuts import redirect
# Create your views here.
def fact_show(request):
    facts = Fact.objects.all()
    return render(request, 'fact_bot_portal/fact_show.html', {'facts': facts})

def fact_new(request):
    if request.method == "POST":
        form = FactForm(request.POST)
        if form.is_valid():
            fact = form.save(commit=False)
            fact.save()
            return redirect('/')
    else:
        form = FactForm()
    return render(request, 'fact_bot_portal/fact_edit.html', {'form': form})
