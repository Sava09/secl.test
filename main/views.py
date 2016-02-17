from django.http.response import HttpResponse

from main.decorators import static_vars
from main.models import ListObject


@static_vars(obj_index=0)
def index(request):
    if index.obj_index >= ListObject.objects.count():
        index.obj_index = 0
        obj = ListObject.objects.filter(processed=False)[index.obj_index]
        index.obj_index += 1
    else:
        obj = ListObject.objects.filter(processed=False)[index.obj_index]
        index.obj_index += 1
    print('ID: ' + str(obj.id) + ', Name: ' + obj.name)
    return HttpResponse(request)
