from django.http import HttpResponse
from django.template import loader


def theme(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())
