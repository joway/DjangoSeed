from django.shortcuts import render


# Create your views here.

def social(request):
    path = request.GET.get('next', '')
    if request.method == 'GET':
        return render(request, 'social.html', locals())
