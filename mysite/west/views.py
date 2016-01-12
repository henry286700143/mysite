from django.http import HttpResponse

def first_page(request):
    return HttpResponse("<p>西餐</p>")
# Create your views here.
