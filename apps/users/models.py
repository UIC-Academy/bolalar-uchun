from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from apps.common.models import BaseModel
from apps.users.choices import ReasonDeleteChoices
from apps.users.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    phone_number = models.CharField(
        unique=True, 
        max_length=50,  # Increased to accommodate suffix
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    reason_delete_choices = models.CharField(choices=ReasonDeleteChoices.choices, null=True, blank=True)
    reason_delete_str = models.CharField(max_length=100, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = [
        "username"
    ]  # username is also required, we'll ask while registration

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

        constraints = [
            models.UniqueConstraint(
                fields=['username'],
                condition=models.Q(is_deleted=False),
                name='unique_active_username'
            ),
        ]

    def delete_account(self):
        """Soft delete user account"""
        from django.utils import timezone
        timestamp = int(timezone.now().timestamp())
        
        # Bypass validation by saving with update_fields
        self.phone_number = f"{self.phone_number}_deleted_{timestamp}"
        self.is_deleted = True
        self.save(update_fields=['phone_number', 'is_deleted'])