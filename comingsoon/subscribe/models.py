from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return "email %s" % (self.email,)

    def __str__(self):
        return self.email


    class Meta:
        ordering = [ "id" ]