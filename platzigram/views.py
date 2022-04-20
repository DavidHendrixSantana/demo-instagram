from email import message
import numbers
from django.http import HttpResponse, JsonResponse
from  datetime import datetime

def hello_world(request):
    return HttpResponse('Current SERVER TIME:  is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))
    
def sort_integer(request):
    numbers = map(lambda x : int(x), request.GET["numbers"].split(","))
    return JsonResponse({ "numbers" : sorted(numbers)} ,json_dumps_params={'indent': 4})


def hi(request, name, age):
    if age > 12:
        message = 'Sorry {}, you are not allowrd'.format(name)
    else:
        message = 'Sorry {}, you are welcome'.format(name)
        
    return HttpResponse(message) 