from django.shortcuts import render

from .models import Result, Profile, Keyword


def result_list(request):
    results = Result.objects.all()
    return render(request, 'result_list.html', {'results': results})


def result_detail(request, pk):
    result = Result.objects.get(id=pk)
    return render(request, 'result_detail.html', {'result': result})
