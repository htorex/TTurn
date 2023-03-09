from django.db import models

from usersdate.models import User
from products.models import Product

from django.db.models.signals import pre_save

import uuid

class Cart(models.Model):

    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, null=True, blank= True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.cart_id
    

def set_cart_id(sender, instance, *arg, **kwargs):

    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())

pre_save.connect(set_cart_id, sender=Cart)