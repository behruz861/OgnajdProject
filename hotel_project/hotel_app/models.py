from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Room(models.Model):
    CATEGORY_CHOICES = [
        ('cheap', 'Дешевые'),
        ('comfortable', 'Удобные'),
        ('vip', 'V.I.P')
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    is_reserved = models.BooleanField(default=False)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)



class Client(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()

class BookApplication(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    additional_services = models.TextField()
    is_approved = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

@receiver(pre_save, sender=BookApplication)
def pre_save_book_application_slug(sender, instance, **kwargs):
    instance.slug = instance.slug or slugify(instance.room.description)[:50]

