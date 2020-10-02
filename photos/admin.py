from django.contrib import admin
from .models import Image,Location,Category
from django.utils.html import format_html

# Register your models here.
# admin.site.register(Image)
def change_image_button(obj):
    return format_html('<a class="btn" href="/admin/photos/image/{}/change/">Change</a>', obj.id)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=["name","slug","location","image" ,change_image_button]
    # list_editable=["name","slug","image"]
    list_display_links=["location"]
    filter_horizontal=["category"]
    prepopulated_fields={"slug":("name",)}

    
admin.site.register(Location)
admin.site.register(Category)

