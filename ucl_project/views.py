from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    context = {
        'title': 'UEFA Chamions League after 4th matchday'
    }
    return render(request, 'index.html', context)



def results(request):
    context = {
        'result': 'Results of matches'
    }
    return render(request, 'result.html', context)



def standing(request):
    context = {
        'standing': 'Teams standing'
    }
    return render(request, 'standing.html', context)