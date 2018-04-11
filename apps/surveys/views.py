
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'counter' not in request.session:
    request.session['counter'] = 0
    return render(request, 'surveys/index.html')
def submit(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name'] 
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment'] 
    return redirect('process/result')
def result(request):
    request.session['counter'] +=1
    info = {
            'name': request.session['name'], 
            'location' :request.session['location'],
            'language': request.session['language'],
            'comment': request.session['comment'], 
            }
    return render(request, 'surveys/result.html', info)
