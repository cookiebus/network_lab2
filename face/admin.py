from django.contrib import admin
from face.models import Person, Photo


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'face_id', 'url')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', )

admin.site.register(Person, PersonAdmin)
admin.site.register(Photo, PhotoAdmin)
