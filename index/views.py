from django.shortcuts import render


# Create your views here.
def index(request, *args, **kwargs):
    template_name = 'base.html'

    return render(request, template_name=template_name)