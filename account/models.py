from typing import Any, Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save



class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=32,null =True)

    class Role(models.TextChoices):
       CLIENT = "CLIENT","client"
       MARCHAND = "MARCHAND","marchand"
       ADMIN = "ADMIN","admin"
    role = models.CharField( max_length=32,choices =Role.choices,default="")
    
   #  REQUIRED_FIELDS =['first_name','last_name']
   #  USERNAME_FIELD = 'email'
   #  EMAIL_FIELD = 'email'



class ClientManager(models.Manager):
   def get_queryset(self,*arg,**kwargs) -> models.QuerySet:
      return super().get_queryset(*arg,**kwargs).filter(role=CustomUser.Role.CLIENT)    
#table des clients
class Client(CustomUser):
  objects = ClientManager()
  class Meta:
     proxy = True
  def save(self,*args,**kwargs) -> None:
      if not self.pk:
        self.role = CustomUser.Role.CLIENT
      return super().save(*args,**kwargs)

    # user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='client')
    # base_role = CustomUser.Role.CLIENT

#class de management pour filtre les marchand
class MarchandManager(models.Manager):
   def get_queryset(self,*arg,**kwargs) -> models.QuerySet:
      return super().get_queryset(*arg,**kwargs).filter(role=CustomUser.Role.MARCHAND)    
#table des marchands
class Marchand(CustomUser):
  objects = MarchandManager()

  class Meta:
     proxy = True
  
  def save(self,*args,**kwargs) -> None:
      if not self.pk:
        self.role = CustomUser.Role.MARCHAND
      return super().save(*args,**kwargs)



#class de management pour filtre les admins
class AdminManager(models.Manager):
   def get_queryset(self,*arg,**kwargs) -> models.QuerySet:
      return super().get_queryset(*arg,**kwargs).filter(role=CustomUser.Role.ADMIN)    


#table des administarteurs 
class Admin(CustomUser):
  objects = AdminManager()
  class Meta:
     proxy = True

  def save(self,*args,**kwargs) -> None:
      if not self.pk:
        self.role = CustomUser.Role.ADMIN
      return super().save(*args,**kwargs)





