from django.db import models

class Exhibit(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_begin = models.DateField()
    date_end = models.DateField()
    owner = models.ForeignKey(User)
    
class NFC(models.Model):
    serial = models.CharField(max_length=50)
    in_use = models.BooleanField()

class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=50)
    release_date = models.DateField()
    photo = models.ImageField(path__to="images/items/")
    nfc_tag = models.ForeignKey(NFC)
    exhibit = models.ManyToManyField(Exhibit)
    
class Experience(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(user)
    confirmed = models.BooleanField()
    hash_url = models.CharField(max_length=40)
    
    def hashit(self):
        from hashlib import sha1
        return sha1(self.pk).hexdigest()

class Comment(models.Model):
    content = models.TextField()
    
class Photo(models.Model):
    content = models.ImageField(path__to="images/userphoto/")
    
class Scan(models.Model):
    content = models.ForeignKey(Item)
    
class Action(models.Model):
    date_performed = models.DateTimeField()
    scan = models.ForeignKey(Scan)
    photo = models.ForeignKey(Photo)
    comment = models.ForeignKey(Comment)
