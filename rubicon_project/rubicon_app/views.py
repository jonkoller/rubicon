from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def home(request):
    # home page
    template = loader.get_template('rubicon_app/home.html')
    context = {'user':'user',}
    return HttpResponse(template.render(context,request))
