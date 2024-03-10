from django.db import models

# Create your models here.
class charityDetails(models.Model):
    org_name=models.CharField(max_length=100)
    purpose=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    ORG_TYPE=[
        ('oldage','Old-Age'),
        ('children','Children'),
    ]
    org_type=models.CharField(max_length=20,choices=ORG_TYPE, default='oldage')


    def __str__(self):
        return self.charity_details





class charityDetails1(models.Model):
    org_name=models.CharField(max_length=100)
    purpose=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    # ORG_TYPE=[
    #     ('oldage','Old-Age'),
    #     ('children','Children'),
    # ]
    # org_type=models.CharField(max_length=20,choices=ORG_TYPE,default='oldage')
    # class meta:
    #     db_table='charities'


    def __str__(self):
        return self.charity_details


class charityDetails2(models.Model):
    org_name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # ORG_TYPE = [
    #     ('oldage', 'Old-Age'),
    #     ('children', 'Children'),
    # ]
    # org_type = models.CharField(max_length=20, choices=ORG_TYPE, default='oldage')

    def __str__(self):
        return self.charity_details