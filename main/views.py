from django.http.response import HttpResponse

from main.decorators import static_vars
from main.models import ListObject


@static_vars(obj_index=0)
def index(request):
    if index.obj_index >= ListObject.objects.filter(processed=False).count():
        index.obj_index = 0
        obj = ListObject.objects.filter(processed=False)[index.obj_index]
        index.obj_index += 1
    else:
        obj = ListObject.objects.filter(processed=False)[index.obj_index]
        index.obj_index += 1
    print('ID: ' + str(obj.id) + ', Name: ' + obj.name)
    return HttpResponse(request)


def process(request, list_object_id):
    try:
        process_obj = ListObject.objects.get(id=list_object_id, processed=False)
        if request.GET:
            if request.GET.get('processed') == 'true':
                process_obj.processed = True
                process_obj.save()
                print(1)
    except:
        print(0)
    return HttpResponse(request)
