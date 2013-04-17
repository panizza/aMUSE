from django.shortcuts import render
from basetyzer.models import Exhibit, Item
from django.shortcuts import get_object_or_404
from ajaxutils.decorators import ajax


@ajax(require="GET")
def home(request):
    """
    Show home page
    """
    exhibitions = Exhibit.objects.available()
    return render(request, 'kiosk/index.html', {
        'exhibition_list': exhibitions
    })

@ajax(require="GET")
def exhibit_item_list(request, id_exhibition):
    exhibition = get_object_or_404(Exhibit, pk=id_exhibition)
    items = exhibition.item_set.all()
    return render(request, 'kiosk/exhibit_item_list.html', {
        'item_list': items,
        'exhibit': exhibition
    })

def item_info(request, id_item):
    item = get_object_or_404(Item, pk=id_item)
    return render(request, 'kiosk/item_info.html', {
        'item': item,
    })