from django.shortcuts import render

def data(request):
    return render(request, 'main_1/data.html')

def test(request):
    return render(request, 'main_1/test.html')
