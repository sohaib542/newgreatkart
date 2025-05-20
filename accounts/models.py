from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self,username,firstname,lastname,email,password=None):
        if not email:
            raise ValueError("Please Enter vaild email address :")
        if not username:
            raise ValueError("please Enter vaild username :")
        user = self.model(username=username,email=self.normalize_email(email),firstname=firstname,lastname=lastname) 
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,firstname,lastname,email,password):
        user=self.create_user(email= self.normalize_email(email),username=username,firstname=firstname,lastname=lastname,password=password)
        user.is_active=True
        user.is_admin=True
        user.is_superadmin=True
        user.is_staff=True
        
        user.save(using=self._db)

class Account(AbstractBaseUser):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=50)

    #required

    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['firstname','lastname','username']

    objects=MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,object=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True
    
