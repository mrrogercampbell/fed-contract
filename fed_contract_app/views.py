from django.shortcuts import render

from .models import Result, Profile, Keyword

def result_list(request):
    results = Result.objects.all()
    return render(request, 'result_list.html', {'results': results})