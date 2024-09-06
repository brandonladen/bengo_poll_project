from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'candidates.html')

def vote_results(request):
    return render(request, 'results.html')

def contact_details(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')