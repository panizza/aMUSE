from django.db import models
from django.contrib.auth.models import User

class Exhibit(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_begin = models.DateField()
    date_end = models.DateField()
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return "%s" % (self.name,)
    
class NFC(models.Model):
    serial = models.CharField(max_length=50)
    in_use = models.BooleanField()

    def __unicode__(self):
        return "%s" % (self.serial,)

class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=50)
    release_date = models.DateField()
    photo = models.ImageField(upload_to="images/items/")
    nfc_tag = models.ForeignKey(NFC)
    exhibit = models.ManyToManyField(Exhibit)

    def __unicode__(self):
        return "%s" % (self.title,)
    
class Experience(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User)
    confirmed = models.BooleanField()
    hash_url = models.CharField(max_length=40)

    def __unicode__(self):
        return "%s - %s" % (self.user.username, self.date,)
    
    def hashit(self):
        from hashlib import sha1
        return sha1(self.pk).hexdigest()


class Comment(models.Model):
    content = models.TextField()

    def __unicode__(self):
        return "%s" % (self.content,)


class Photo(models.Model):
    content = models.ImageField(upload_to="images/userphoto/")

    def __unicode__(self):
        return "%s" % (self.content.name,)


class Scan(models.Model):
    content = models.ForeignKey(Item)

    def __unicode__(self):
        return "%s" % (self.content,)


class Action(models.Model):
    date_performed = models.DateTimeField()
    scan = models.ForeignKey(Scan)
    photo = models.ForeignKey(Photo)
    comment = models.ForeignKey(Comment)
    experience = models.ForeignKey(Experience)

    def __unicode__(self):
        return "%s" % (self.experience, self.date)