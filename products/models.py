from datetime import datetime
from django.db import models
from django.utils.text import slugify 
from django.contrib.auth.models import User
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)
    parent_id = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)
    description = models.TextField(null=False, blank=False)
    price = models.FloatField()
    image = models.ImageField(upload_to='products')
    quantity = models.IntegerField()
    available = models.BooleanField(null=False)
    brand = models.CharField(max_length=150, null=False, blank=False)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now(), editable=False)

    # def save(self):
    #     super().save()
        # img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300 :
        #     new_img = (300,300)
        #     img.thumbnail(new_img)
        #     img.save(self.image.path)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300 :
            new_img = (300,300)
            img.thumbnail(new_img)
            img.save(self.image.path)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"<User> {self.user.username} <Product> {self.product.name}"

    def save(self, *args, **kwargs):
        self.total = self.product.price * self.quantity
        return super(Cart, self).save(*args, **kwargs)

# class Delivery_Details(models.Model):
    


