from piston.handler import BaseHandler
from basetyzer.models import Item

class ItemHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Item
    fields = ('description', 'author', 'photo', 'release_date', 'title', 'id',
              ('nfc_tag', ('serial', 'id', 'in_use'))
    )
    #exclude = ('_state')
    def read(self, request, item_id):
        return Item.objects.get(id=item_id)
        
