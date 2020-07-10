from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {})

def read(request):
    return

def create(request):
    return
    
def update(request, pk):
    return
    
def delete(request, pk):
    return