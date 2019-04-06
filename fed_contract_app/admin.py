from django.contrib import admin
from .models import Result
from .models import Profile
from .models import Keyword

admin.site.register(Result)
admin.site.register(Profile)
admin.site.register(Keyword)