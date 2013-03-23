from django.contrib import admin
from basetyzer.models import Item, Exhibit, CustomUser, SuperQRCode
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

class CustomUserAdmin(admin.ModelAdmin):
    #TODO[panizza]: modificare e dividere visivamente le info
    list_display = ["username", "email", "is_staff"]


class ExhibitAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Exhibition", dict(
                classes=("wide",),
                fields=["name", ]
            )
        ),
        (
            "Dates", dict(fields=["date_begin", "date_end"])
        ),
        (
            "Other", dict(fields=["owner"])
        ),
    )
    list_filter = ["date_end"]
    list_display = ("name", "description", "date_begin", "date_end",)
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
    list_display = ("title", "description", "author" )
    search_fields = ["title", "author"]
    readonly_fields = ('tag',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Exhibit, ExhibitAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.unregister(Group)
admin.site.unregister(Site)

admin.site.register(SuperQRCode)