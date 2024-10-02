from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Images(models.Model):
    bg1_image = models.ImageField(upload_to='assests/upload', default="", blank="True")
    bg2_image = models.ImageField(upload_to='assests/upload', default="", blank="True")
    bg3_image = models.ImageField(upload_to='assests/upload', default="", blank="True")
    worker1_image = models.ImageField(upload_to='assests/upload', default="", blank="True")
    worker2_image = models.ImageField(upload_to='assests/upload', default="", blank="True")
    worker3_image = models.ImageField(upload_to='assests/upload', default="", blank="True")

class Clients(models.Model):
    client_id = models.AutoField
    client_name = models.CharField(max_length=50)
    client_image = models.ImageField(upload_to='assests/upload', default="")

    def __str__(self):
        return self.client_name

class Franchise(models.Model):
    franchise_id = models.AutoField
    franchise_name = models.CharField(max_length=50)
    franchise_image = models.ImageField(upload_to='assests/upload', default="")

    def __str__(self):
        return self.franchise_name


class Products(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=1000, blank='True')
    product_spec1 = models.CharField(max_length=100, default="")
    product_spec2 = models.CharField(max_length=100, default="")
    product_spec3 = models.CharField(max_length=100, default="", blank='True')
    product_spec4 = models.CharField(max_length=100, default="", blank='True')
    product_spec5 = models.CharField(max_length=100, default="", blank='True')
    product_spec6 = models.CharField(max_length=100, default="", blank='True')
    product_spec7 = models.CharField(max_length=100, default="", blank='True')
    product_spec8 = models.CharField(max_length=100, default="", blank='True')
    product_spec9 = models.CharField(max_length=100, default="", blank='True')
    product_spec10 = models.CharField(max_length=100, default="", blank='True')
    image = models.ImageField(upload_to='assests/upload', default="")


    def __str__(self):
        return self.product_name

class Machines(models.Model):
    Machine_id = models.AutoField
    Machine_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,blank=True)
    Machine_image = models.ImageField(upload_to='assests/upload', default="")

    def __str__(self):
        return self.Machine_name

class Credentials(models.Model):
    Credential_id = models.AutoField
    Credential_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,blank=True)
    Credential_image = models.ImageField(upload_to='assests/upload', default="")

    def __str__(self):
        return self.Credential_name


class Contact(models.Model):
    Contact_id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = PhoneNumberField()
    msg = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Enquiry(models.Model):
    Enquiry_id = models.AutoField
    name = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = PhoneNumberField()
    msg = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name + self.product_name

