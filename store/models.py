from django.db import models
import uuid
from app.models import  *
# Create your models here.

class Cathegorie(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Cathegorie/images/',null=True)
    id_modele= models.ForeignKey(Modele,on_delete=models.CASCADE,default="" 
                                 )
    

class Piece(models.Model):
    id_cathegorie =  models.ForeignKey(Cathegorie,on_delete=models.CASCADE,default="",blank=True,null=True)
    name =models.CharField(max_length=255, )
    price = models.FloatField(null=True)
    qt_stock = models.IntegerField( null=True)
    # brand = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Pieces/images/', null=True)
    city = models.CharField(max_length=255, null=True)
    # type = models.CharField(max_length=255)
    description = models.TextField(null=True )


    def __str__(self):
        return self.name


class Commande(models.Model):
    # pk_comment  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_price = models.FloatField( null=True, default=0)
    commande_date = models.DateField(auto_now_add=True)
    Statut = models.BooleanField(default=False)
    piece  = models.ManyToManyField(Piece,default=0,related_name = 'product_commande')

