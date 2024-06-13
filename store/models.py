from django.db import models
import uuid
from app.models import  *
from django.dispatch import receiver
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Permission,Group
from account.models import Marchand,OtherClient

class Cathegorie(models.Model):
    name = models.CharField(max_length=255)
    thumbs  = models.ImageField(upload_to='Cathegorie/images/', blank=True)
    id_modele= models.ManyToManyField(Modele,related_name='cathegories'
                                 )
    def __str__(self):
        return self.name


class  Piece(models.Model):
    id_marchand = models.ForeignKey(Marchand,on_delete=models.CASCADE,blank=True,default=1,related_name='pieces')
    id_cathegorie =  models.ForeignKey(Cathegorie,on_delete=models.CASCADE, blank=True,default=1,related_name='pieces')
    id_marque = models.ForeignKey(Marque,on_delete=models.CASCADE,related_name='marque',default=1,null=True,)
    modele = models.CharField(max_length=512,default='4x4')
    name =models.CharField(max_length=255)
    price = models.FloatField( blank=True)
    qt_stock = models.IntegerField(  blank=True)
    # brand = models.CharField(max_length=255)
    # thumbs = models.ImageField(upload_to='Pieces/images/', blank=True)
    city = models.CharField(max_length=255,default='yaounde')
    # type = models.CharField(max_length=255)
    description = models.TextField( blank=True )

class PieceImage(models.Model):
    thumbs = models.ForeignKey(Piece,on_delete=models.CASCADE,blank=True,related_name='thumbs')
    piece_image = models.ImageField(upload_to='Pieces/images/', blank=True,default='')
    image_url = models.CharField(max_length=255,blank = True, default='')
    public_id = models.CharField(max_length=255,blank= True ,default = '')
    

    def __str__(self):
        return self.image_url


class Commande(models.Model):
    # pk_comment  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_id = models.ForeignKey(OtherClient,on_delete=models.CASCADE,related_name='commande_id',blank=True)
    total_price = models.FloatField(  blank=True, default=0)
    commande_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    operator = models.CharField(max_length = 256)
    transaction_id = models.CharField(max_length=256)
    piece  = models.ManyToManyField(Piece,default=0,related_name = 'commandes')
    piece_qte = models.CharField(max_length=256)



#this function is use to assign permission can_create_cathegorie  to all Marchand model
#after  the dabase migrate
# @receiver(post_migrate)
# def assign_permissions_cathegorie(sender,**kwargs):
#     add_marque = Permission.objects.get(codename = 'add_marque')
#     change_marque = Permission.objects.get(codename='change_marque')
#     delete_marque = Permission.objects.get(codename='delete_marque')

#     add_modele = Permission.objects.get(codename = 'add_modele')
#     change_modele = Permission.objects.get(codename='change_modele')
#     delete_modele = Permission.objects.get(codename='delete_modele')

#     add_cathegorie = Permission.objects.get(codename='add_cathegorie')
#     change_cathegorie = Permission.objects.get(codename='change_cathegorie')
#     delete_cathegorie = Permission.objects.get(codename='delete_cathegorie')

#     add_piece = Permission.objects.get(codename='add_piece')
#     change_piece = Permission.objects.get(codename='change_piece')
#     delete_piece = Permission.objects.get(codename='delete_piece')

#     create_permission=[
#         add_marque,
#         change_marque,
#         delete_marque,

#         add_modele,
#         change_modele,
#         delete_modele,

#         add_cathegorie,
#         change_cathegorie,
#         delete_cathegorie,

#         add_piece,
#         change_piece,
#         delete_piece,
#     ]

#     marchand_Gourp_Permissionss =Group(name='marchand_Gourp_Permissionss')
#     marchand_Gourp_Permissionss.save()
#     marchand_Gourp_Permissionss.permissions.set(create_permission)
