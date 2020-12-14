from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.HouseRule, models.Facility, models.Amenity)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """
    list_display = ("name", "user_by")

    def user_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    fieldsets = (
        ("Basic Info", {
            "fields": (
                "name",
                "description",
                "country",
                "city",
                "price",
                "room_type",
            )
        }),
        ("Time", {
            "fields": (
                "check_in",
                "check_out",
                "instant_book",
            )
        }),
        ("More About the Space",  {
            'classes': ('collapse',),
            "fields": (
                "amenity",
                "facility",
                "house_rule",
            )
        }),
        ("Spaces", {
            "fields": (
                "guests",
                "beds",
                "bedrooms",
                "baths",
            ),
        }),
        ("Last Details", {
            "fields": (
                "host",
            ),
        }),
    )

    list_display = (
        "name",
        "country",
        "city",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "room_type",
        "count_amenities",
        "count_facilities",
        "count_photo",
        "total_rating"

    )

    list_filter = (
        "instant_book",
        "room_type",
        "country",
        "city",
    )
    search_fields = ("=city", "^host__username")

    filter_horizontal = (
        "amenity",
        "facility",
        "house_rule",
    )

    def count_amenities(self, obj):
        return obj.amenity.count()
    count_amenities.short_description = "ame"

    def count_facilities(self, obj):
        return obj.facility.count()
    count_facilities.short_description = "faci"

    def count_photo(self, obj):
        return obj.photos.count()
    count_photo.short_description = "photo"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """
    pass
