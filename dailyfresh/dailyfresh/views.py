from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "others/about.html")

def contact(request):
    return render(request, "others/contact.html")

# def page_not_found(request):
#     return render(request, '404.html')
#
#
# def page_error(request):
#     return render(request, '500.html')
#
#
# def permission_denied(request):
#     return render(request, '403.html')