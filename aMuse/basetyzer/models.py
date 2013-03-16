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

    class Meta:
        ordering = ['date_begin']


class Tag(models.Model):
    serial = models.CharField(max_length=50)
    in_use = models.BooleanField(editable=False)

    def __unicode__(self):
        return "%s" % (self.serial,)

class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=50)
    release_date = models.DateField()
    photo = models.ImageField(upload_to="images/items/")
    tag = models.ForeignKey(Tag, null=False, default=None)
    exhibit = models.ManyToManyField(Exhibit)

    def __unicode__(self):
        return "%s" % (self.title,)

    class Meta:
        ordering = ['pk']


class Experience(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    confirmed = models.BooleanField(default=False)
    hash_url = models.CharField(max_length=40, default='', editable=False)

    def __unicode__(self):
        return "%s - %s" % (self.user.username, self.date,)

    class Meta:
        ordering = ['date']

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
    scan = models.ForeignKey(Scan, null=True, default=None)
    comment = models.ForeignKey(Comment, null=True, default=None)
    photo = models.ForeignKey(Photo, null=True, default=None)
    experience = models.ForeignKey(Experience)

    def __unicode__(self):
        return "%s" % (self.experience)

    class Meta:
        ordering = ['experience', 'date_performed']
