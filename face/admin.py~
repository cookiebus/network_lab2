from django.contrib import admin
from face.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'face_id')


admin.site.register(Person, PersonAdmin)
