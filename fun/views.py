from django.shortcuts import render

# Create your views here.
def fun_index(request):
    return render(request, 'fun_index.html', {})