from django.db import models

# Create your models here.
class Exchange(models.Model):
    cur_unit = models.TextField(unique=True)
    cur_nm = models.TextField()
    tts = models.TextField()
    deal_bas_r = models.TextField()

class BankAddress(models.Model):
    sido = models.CharField(max_length=10)
    sigungu = models.CharField(max_length=10)

class BankName(models.Model):
    kor_co_nm = models.TextField()