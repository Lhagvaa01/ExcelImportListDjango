
from django.db import models
from django.db.models import CASCADE
from django.utils.timezone import now


class VoicherPrice(models.Model):
    name = models.CharField(default="Нэр", max_length=255)
    price = models.IntegerField(default=0 )


class Users(models.Model):
    TCUSERICON = models.ImageField(upload_to='photos/', blank=True, null=True)
    TCUSERNAME = models.CharField(help_text="Хэрэглэгчийн нэр", max_length=100, blank=False)
    TCPHONE = models.IntegerField(help_text="Нууц үг", null=True, blank=True)
    TCPASSWORD = models.CharField(help_text="Нууц үг", max_length=100, blank=False)
    TCEMAIL = models.CharField(help_text="Имэйл хаяг", max_length=100, blank= False, unique=True)
    otp = models.IntegerField(help_text="OTP CODE", null=True, blank=True, editable=False)

    def __str__(self):
        return self.TCUSERNAME




class ProductList(models.Model):
    TCITEMCODE = models.CharField(help_text="Dotood kod", max_length=100, blank=False)
    TCNAME = models.CharField(help_text="Ner", max_length=100, blank=False)
    TCGROUP = models.CharField(help_text="Tasag", max_length=100, blank=False)
    TCSALEPRICE = models.IntegerField(help_text="Sale Price", null=True, blank=True)
    TCVOUCHERPRICEPk = models.ForeignKey(VoicherPrice, on_delete = CASCADE)
    TCBARCODE = models.IntegerField(help_text="Barcode", null=True, blank=True)


    def __str__(self):
        return self.TCITEMCODE
  
