from django.shortcuts import render

# Vista del Home
def home(request):
    return render(request, 'index.html')