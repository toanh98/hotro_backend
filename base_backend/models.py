from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

#  Custom User Model
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The username field must be set")
        username = self.normalize_email(username)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(username, password, **extra_fields)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    role_name = models.CharField(max_length=50,null=False,default='Nhân viên y tế')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "username"

    class Meta:
        db_table = "Users"


class Hostpital(models.Model):
    hostpitalName = models.CharField(max_length=200,null=False)
    hostpitalCode = models.CharField(max_length=30,null=False)
    latitude = models.CharField(null=True,max_length=200)
    longitude = models.CharField(null=True,max_length=200)
    class Meta:
        db_table='Hostpital'
        indexes = [
            models.Index(
                fields=[
                    'hostpitalCode',
                ]
            )
        ]

class ProfileUser(models.Model):
    hostpitalId = models.OneToOneField(
        Hostpital,
        on_delete=models.SET_NULL,
        null=True,
        related_name='hostpitalId',
        db_column = 'hostpitalId'
        )
    userId = models.OneToOneField(
        UserAccount,
        on_delete = models.CASCADE,
        related_name = 'userId',
        db_column = 'userId'
    )
    class Meta:
        db_table = 'ProfileUser'
        indexes = [
            models.Index(
                fields=[
                    'hostpitalId',
                    ]
                )
        ]

class RequestType(models.Model):
    pass

class InformationRequest(models.Model):
    requestProfileUserId = models.ForeignKey(
        ProfileUser,
        on_delete = models.DO_NOTHING
    )