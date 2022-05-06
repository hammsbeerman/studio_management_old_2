from time import time
from django.db import models
from django.conf import settings
from django.urls import reverse
from inventory.utils import number_str_to_float
from inventory.validators import validate_unit_of_measure
from customers.models import Customer, Contact
from inventory.models import NonInventory, Inventory, Service
#import pint

# Create your models here.
class Scratch(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, blank=True, null=True, on_delete=models.SET_NULL)
    #company = models.OneToOneField(Customer, on_delete=models.CASCADE, blank=True, null=True)
    workorder = models.CharField('Workorder', max_length=100, blank=False, null=False)
    description = models.TextField('Description', max_length=100, blank=True, null=True)
    deadline = models.CharField('Deadline', max_length=100, blank=True, null=True)
    budget = models.CharField('Budget', max_length=100, blank=True, null=True)
    quoted_price = models.CharField('Quoted Price', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.workorder

    def get_absolute_url(self):
        #return "/pantry/recipes/"
        return reverse("scratch:detail", kwargs={"id": self.workorder})

    def get_edit_url(self): #reference these, that way changes are only made one place
        return reverse("scratch:update", kwargs={"id": self.id})

    def get_contacts_children(self):
        return self.contact_set.all()

    def get_services_children(self):
        return self.workorderservice_set.all()

    def get_inventory_children(self):
        return self.workorderinventoryproduct_set.all()

    def get_noninventory_children(self):
        return self.workordernoninventoryproduct_set.all()

