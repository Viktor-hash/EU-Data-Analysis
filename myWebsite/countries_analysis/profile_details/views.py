from django.http import HttpResponse
from django.template import loader


def profileDetails(request):
    template = loader.get_template('test.html')
    return HttpResponse(template.render())
