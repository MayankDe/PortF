from django.db import models

from django.db import models
from ckeditor.fields import RichTextField

from datetime import *
# from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class PersonalInformation(models.Model):
    name_complete = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.FileField( upload_to='avatar', max_length=100, null=True)
    mini_about = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    cv = models.FileField(upload_to='cv', blank=True, null=True)

    # Social Network
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    mycv = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name_complete


class About(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    description1 = models.TextField(blank=False, null=True)
    description2 = models.TextField(blank=False, null=True)
    about_avatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    skill = models.TextField(max_length=230, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.FileField( upload_to='media', max_length=100, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)

    email = models.EmailField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    msg = models.TextField(max_length=100, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Skills(models.Model):
    skill = models.CharField(max_length=50, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.skill



class Contact(models.Model):
    full_name = models.CharField( _("full_name"),max_length=150, null=True)
    email = models.CharField(_("email"), max_length=100,null = False,default="mayankdehariya200@gmail.com")
    subject = models.CharField(_("subject"),max_length=255,null=True)
    message = models.TextField(_("message"),default="We will meet soon!")
    time_stamp = models.DateTimeField( default=datetime.now )
    

    def __str__(self):
        return self.email