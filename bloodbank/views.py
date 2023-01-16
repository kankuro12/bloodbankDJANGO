from django.http import HttpResponse

def data(request):
    return HttpResponse("Hello, world. You're at the polls index.")
