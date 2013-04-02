from django.contrib import admin
from basetyzer.models import Item, Exhibit, CustomUser
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from sorl.thumbnail.admin import AdminImageMixin


class NoPermissionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    actions = None


class CustomUserAdmin(NoPermissionAdmin):
    #TODO[panizza]: modificare e dividere visivamente le info
    list_display = ['username', 'email', 'is_staff', 'need_reset']


class ExhibitAdmin(admin.ModelAdmin):
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


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Exhibit, ExhibitAdmin)
admin.site.register(Item, ItemAdmin)

admin.site.unregister(Group)
admin.site.unregister(Site)
