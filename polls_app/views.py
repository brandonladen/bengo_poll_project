from django.shortcuts import render
from .models import candidate

# Create your views here.
def landing_page(request):
    return render(request, 'index.html')

def home(request):
    candidates = candidate.objects.all() #select * from candidate;

    context = {
        'candidates': candidates
    }
    return render(request, 'candidates.html', context)

def vote_results(request):
    return render(request, 'results.html')

def contact_details(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')