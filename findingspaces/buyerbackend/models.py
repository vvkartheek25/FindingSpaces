from django.db import models

class BuyerBackend(models.Model):
    buyer_id = models.IntegerField()
    sq_ft = models.IntegerField()
    price = models.IntegerField()
