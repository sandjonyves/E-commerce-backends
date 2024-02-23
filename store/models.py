from django.db import models
import uuid
from app.models import  *
# Create your models here.

class Cathegorie(models.Model):
    name_Cathegorie = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Cathegorie/images/',null=True)
    id_voiture= models.ForeignKey(Voiture,on_delete=models.CASCADE,default=""
                                 )
    

class Piece(models.Model):
    id_cathegorie =  models.ForeignKey(Cathegorie,on_delete=models.CASCADE,default="")
    name =models.CharField(max_length=255, )
    price = models.FloatField( )
    qt_stock = models.IntegerField( )
    # brand = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Pieces/images/', )
    city = models.CharField(max_length=255, )
    # type = models.CharField(max_length=255)
    description = models.TextField( )


class Commande(models.Model):
    # pk_comment  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_price = models.FloatField( )
    commande_date = models.DateField(auto_now_add=True,null=True)
    Statut = models.BooleanField(default=False)
    piece  = models.ForeignKey(Piece,on_delete=models.PROTECT,default=0)

