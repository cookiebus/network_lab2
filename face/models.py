from django.db import models

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to = u'static/upload')
    class Meta:
		ordering = ('-id', )
  

class Person(models.Model):
    name = models.CharField(u"name", max_length=255)
    major = models.CharField(u"major", max_length=255)
    url = models.URLField(u"Baike", max_length=200)
    face_id = models.CharField(u"face-id", max_length=255, null=True, blank=True)  
    image = models.ImageField(upload_to = u'static/img')

    class Meta:
		ordering = ('-id', )
    
    def __str__(self):
        return u"%s %s" % (self.name, self.major)

    def __unicode__(self):
        return u'%s' % self.__str__()    

