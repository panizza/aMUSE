from django.contrib import admin
from basetyzer.models import Item, Exhibit, Experience, Action
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site
from sorl.thumbnail.admin import AdminImageMixin
from django.contrib.auth.admin import UserAdmin


class NoPermissionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    actions = None

class ExtraUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('has_usable_password',)

    lista = list(UserAdmin.fieldsets[2][1]['fields'])
    lista.remove('user_permissions')
    UserAdmin.fieldsets[2][1]['fields'] = tuple(lista)

    def has_usable_password(self, user):
        return user.has_usable_password()
    has_usable_password.short_description = "Need Reset?"
    has_usable_password.boolean = True

class ExhibitAdmin(AdminImageMixin, admin.ModelAdmin):
    fieldsets = (
        (
            'Exhibition', dict(fields=['name', 'description', 'image'])
        ),
        (
            'Dates', dict(fields=['date_begin', 'date_end'])
        ),
        (
            'Other', dict(fields=['owner'])
        ),
    )
    list_filter = ['name']
    list_display = ('name', 'my_description', 'date_begin', 'date_end', 'is_visitable', )
    search_fields = ['name']

    def my_description(self, exhibit):
        return exhibit.description if len(exhibit.description) <= 250 else exhibit.description[:250].rsplit(' ', 1)[0] + '...'
    my_description.short_description = 'Description'

    def is_visitable(self, exhibit):
        return True if exhibit in Exhibit.objects.available() else False
    is_visitable.boolean = True
    is_visitable.short_description = 'Can visit?'


class ItemAdmin(AdminImageMixin, admin.ModelAdmin):
    fieldsets = (
            (
                'Item Info', dict(fields=['title', 'description', 'author',
                                          'release_date', 'photo'])
            ),
            (
                'Other', dict(classes=('wide',), fields=['exhibit', 'tag'])
            ),
    )
    filter_horizontal = ['exhibit',]
    list_filter = ['exhibit', 'author']
    list_display = ('title', 'description', 'author' )
    search_fields = ['title', 'author']
    readonly_fields = ('tag',)


admin.site.register(Exhibit, ExhibitAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Experience)
admin.site.register(Action)

#$#CHEAT: disattivo la visualizzazione normale di user
admin.site.unregister(User)
admin.site.register(User, ExtraUserAdmin)

admin.site.unregister(Group)
admin.site.unregister(Site)
