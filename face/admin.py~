from django.contrib import admin
from face.models import Person, Photo


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'face_id')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', )

admin.site.register(Person, PersonAdmin)
admin.site.register(Photo, PhotoAdmin)
