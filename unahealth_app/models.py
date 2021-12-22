from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime
import uuid

# Create your models here.

# Custom user Manager class
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, password):
        """ Create Superuser"""
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

# custom User Model
class User(AbstractBaseUser):
    objects = UserManager()
    username = models.CharField(
        verbose_name='Username',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
    
    
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """ Check if user has permission: more an override then anything"""
        return True

    def has_module_perms(self, app_label):
        return True
    
# GlucoseLevel Model class
class GlucoseLevel(models.Model):
    # define as a uuid field
    #serial number 
    seriennummer = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
    )  
    # device
    gerat = models.CharField(max_length=200)
    # device timestamp
    geratezeitstempel = models.DateTimeField(auto_now_add=True)
    #recording type
    aufzeichnungstyp = models.IntegerField()
    #glucose value history
    glukosewert_verlauf = models.IntegerField()
    #glucose scan
    glukose_scan = models.IntegerField()
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.seriennummer)