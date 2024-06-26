from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager


class UserModelManager(UserManager):
    def _create_user(self, phone, email, password, **extra_fields):
        if not phone:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(phone=phone, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone=phone, email=email, password=password, **extra_fields)

    def create_superuser(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("type", 'superuser')

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone, email, password, **extra_fields)


class OperatorProxyManager(UserModelManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=self.model.Type.OPERATOR)


class AdminProxyManager(UserModelManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=self.model.Type.ADMIN)


class ManagerProxyManager(UserModelManager):

    def get_queryset(self):
        return super().get_queryset().filter(type=self.model.Type.MANAGER)


class ClientProxyManager(UserModelManager):

    def get_queryset(self):
        return super().get_queryset().filter(type=self.model.Type.CLIENT)


class CourierProxyManager(UserModelManager):

    def get_queryset(self):
        return super().get_queryset().filter(type=self.model.Type.COURIER)


