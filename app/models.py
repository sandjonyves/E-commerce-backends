from django.db import models

# Create your models here.
class Marque(models.Model):
    name = models.CharField(max_length=255, )
    def __str__(self):
        return self.name

# class Modele(models.Model):
#     name = models.CharField(max_length=255, )
#     id_marque = models.ForeignKey(Marque,on_delete =models.CASCADE,default="")
    
#     def __str__(self):
#         return self.name
# # class Voiture(models.Model):
# #     id_modele = models.ForeignKey(Modele,on_delete=models.CASCADE,default="")
# #     name = models.CharField(max_length=255, )  


