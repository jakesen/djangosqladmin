from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    context = {}
    if request.user.is_authenticated:
        context['databases'] = request.user.database_set.all()
    return render(request, 'databases/dashboard.html', context)
