from django.db import models
from django.conf import settings

# Create your models here.
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    fin_prdt_nm = models.TextField()
    kor_co_nm = models.TextField()
    dcls_month = models.TextField()
    join_way = models.TextField()
    mrtr_int = models.TextField(null=True)
    spcl_cnd = models.TextField()
    join_deny = models.TextField()
    join_member = models.TextField()
    max_limit = models.TextField(null=True)

class DepositCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class DepositOptions06(models.Model):
    fin_prdt_cd = models.TextField()
    save_trm = models.IntegerField()
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)

class DepositOptions12(models.Model):
    fin_prdt_cd = models.TextField()
    save_trm = models.IntegerField()
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)

class DepositOptions24(models.Model):
    fin_prdt_cd = models.TextField()
    save_trm = models.IntegerField()
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)

class DepositOptions36(models.Model):
    fin_prdt_cd = models.TextField()
    save_trm = models.IntegerField()
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)