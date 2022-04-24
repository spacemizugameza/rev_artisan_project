from django.db import models
from django.contrib.auth.models import User 
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus

# Create your models here.
class Delivery_Details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phno = models.CharField(max_length=10,null=False,blank=False)
    address = models.TextField(null=False,blank=False)
    country = models.CharField(max_length=50,null=False,blank=False)
    city = models.CharField(max_length=100,null=False,blank=False)
    state = models.CharField(max_length=50,null=False,blank=False)
    pincode = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.address} {self.city} {self.state} {self.country} {self.pincode}"



class Order(models.Model):
    name = CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"