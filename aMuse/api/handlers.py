from piston.handler import BaseHandler
from basetyzer.models import Item

class ItemHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Item
    #fields = (
    exclude = ('_state')
    def read(self, request, item_id):
        return Item.objects.get(id=item_id)
        
