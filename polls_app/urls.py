from django.urls import path
from .views import landing_page, home, vote_results, contact_details, about

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('home/', home, name="home"),
    path('results/', vote_results, name="results"),
    path('contacts/', contact_details, name="contacts"),
    path('about/', about, name="about"),
]