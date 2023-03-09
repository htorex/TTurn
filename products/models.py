import uuid

from django.db import models

from django.utils.text import slugify
from django.db.models.signals import pre_save

class Product(models.Model):

    dia = models.CharField(max_length=20)
    turno = models.CharField(max_length=20)
    horarios = models.CharField(max_length=20)
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='productsm/', null=False, blank=False)
    
    def __str__(self):
        
        return self.dia

def set_slug(sender, instance, *args, **kwargs):

    if instance.dia and not instance.slug:
        slug = slugify(instance.dia)

        while Product.objects.filter(slug=slug).exists():

            slug = slugify(
                '{}-{}'.format(instance.dia, str(uuid.uuid4())[:8])
            )

        instance.slug = slug

pre_save.connect(set_slug, sender=Product)