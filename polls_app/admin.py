from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(candidate)
admin.site.register(voter)
admin.site.register(votes)
admin.site.register(post)
admin.site.register(political_party)