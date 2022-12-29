from django.db import models

# Create your models here.


class registration(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    uname = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.BigIntegerField()
    psw = models.CharField(max_length=15)

    class Meta:
        db_table = "registration"


class vehicledb(models.Model):
    si = models.IntegerField()
    plate_num = models.CharField(max_length=20)
    dt = models.DateTimeField()

    class Meta:
        db_table = "vehicledb"
