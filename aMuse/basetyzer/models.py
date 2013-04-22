from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
from hashlib import sha1
from sorl import thumbnail
from hashlib import sha1
from django.utils.http import int_to_base36


class ExhibitionManager(models.Manager):
    """
    This class save developers life.
    """
    def available(self):
        """ Return a QuerySet. The QuerySet contains all the Exhibition that
            ends after today and started before today
        """
        return self.get_query_set().exclude(date_end__lt=date.today()).\
            exclude(date_begin__gt=date.today())


class Exhibit(models.Model):
    """
    The main model. This contains pretty much everything
    """
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_begin = models.DateField()
    date_end = models.DateField()
    owner = models.ForeignKey(User)
    image = thumbnail.ImageField(upload_to="images/exhibit/")
    objects = ExhibitionManager()

    def __unicode__(self):
        return "%s" % (self.name,)

    class Meta:
        ordering = ['date_begin']


class Item(models.Model):
    """
    A model containing all the item
    """
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=50)
    release_date = models.DateField()
    photo = thumbnail.ImageField(upload_to="images/items/")
    tag = models.CharField(max_length=40, null=False, blank=True)
    exhibit = models.ManyToManyField(Exhibit)

    def __unicode__(self):
        return "%s" % (self.title,)

    class Meta:
        ordering = ['pk']


class Experience(models.Model):
    """
    Storage for the user's experiences
    """
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    public = models.BooleanField(default=False)
    hash_url = models.CharField(max_length=40, blank=True, null=True)

    def __unicode__(self):
        return "%s - %s" % (self.user.username,
                            self.date.replace(microsecond=0, tzinfo=None),)

    class Meta:
        ordering = ['date']


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
    """
    The Action model is the storage for the real experiences information
    """
    date_performed = models.DateTimeField()
    scan = models.ForeignKey(Scan, null=True, default=None)
    comment = models.ForeignKey(Comment, null=True, default=None)
    photo = models.ForeignKey(Photo, null=True, default=None)
    experience = models.ForeignKey(Experience)

    def __unicode__(self):
        return "%s" % (self.experience,)

    class Meta:
        ordering = ['experience', 'date_performed']


class SuperQRCode(models.Model):
    """
    SuperQRCode contains the current qr_code verification for experiences
    uploads. Number of tuples = 1
    """
    text = models.CharField(max_length=40)
    last_edit = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % (self.text,)

    class Meta:
        verbose_name = "QRCode"


@receiver(post_save, sender=Item)
def item_post_save(sender, **kwargs):
    item = kwargs['instance']
    if not item.tag:
        hash = sha1(str(item.pk)).hexdigest()
        item.tag = hash
        item.save()


@receiver(post_save, sender=Experience)
def experience_post_save(sender, **kwargs):
    experience = kwargs['instance']
    if not experience.hash_url:
        hash_url = "%s-%s" % (int_to_base36(experience.user.pk), sha1(str(experience.pk)).hexdigest())
        experience.hash_url = hash_url
        experience.save()