from django.http import HttpResponse, Http404

def obtain_item_info(request, id):
    """ (no docs)
    """
    return HttpResponse(id)