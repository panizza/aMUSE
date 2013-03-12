from piston.handler import BaseHandler
from basetyzer.models import Item

class ItemHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Item
    fields = ('description', 'author', 'photo', 'release_date', 'title', 'id',
              ('tag', ('serial', 'id', 'in_use'))
    )
    #exclude = ('_state')
    def read(self, request, item_id):
        return Item.objects.get(id=item_id)
        

class ResponseHandler(BaseHandler):
    allowed_method = ('POST',)

    def create(self, request):
        data = request.data