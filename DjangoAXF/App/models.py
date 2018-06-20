from django.db import models

# Create your models here.
class BaseModel(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)

    class Meta:
        abstract=True

class WheelModel(BaseModel):
     class Meta:
         db_table = 'axf_wheel'


class NavModel(BaseModel):
    class Meta:
        db_table = 'axf_nav'

class MustBuyModel(BaseModel):
    class Meta:
        db_table = 'axf_mustbuy'