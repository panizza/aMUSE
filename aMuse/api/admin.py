from django.contrib import admin
from basetyzer.models import Item, Exhibit, Tag, Experience, CustomUser
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

class CustomUserAdmin(admin.ModelAdmin):
    #TODO[panizza]: modificare e dividere visivamente le info
    list_display = ["username", "email", "is_staff"]


class ExhibitAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Exhibition", dict(fields=["name", "description"])
        ),
        (
            "Dates", dict(fields=["date_begin", "date_end"])
        ),
        (
            "Other", dict(fields=["owner"])
        ),
    )
    list_filter = ["date_end"]
    list_display = ("name", "date_begin", "date_end")
    list_display_links = ("name",)
    search_fields = ["name"]


class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
            (
                "Item Info", dict(fields=["title", "description", "author",
                                          "release_date", "photo"])
            ),
            (
                "Other", dict(classes=("wide",), fields=["exhibit", "tag"])
            ),
    )
    filter_vertical = ["exhibit",]
    list_filter = ["exhibit", "author"]
    list_display = ("title", "author", )
    list_display_links = ("title",)
    search_fields = ["title", "author"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Exhibit, ExhibitAdmin)
admin.site.register(Item, ItemAdmin)

admin.site.unregister(Group)
admin.site.unregister(Site)