from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.urls import reverse


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, phone, password=None, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone:
            raise ValueError('The given phone must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    phone = models.CharField(max_length=11, unique=True, verbose_name='شماره موبایل', blank=False,
                             help_text='Enter 11 digits phone number')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class PhoneOTP(models.Model):
    phone = models.CharField(max_length=11, null=True)
    otp = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    Man = 1
    Woman = 2
    STATUS_CHOICES = ((Man, 'مرد'), (Woman, "زن"))
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    gender = models.IntegerField(choices=STATUS_CHOICES, verbose_name='جنسیت')
    email = models.EmailField(max_length=200, blank=True, unique=True, default=None, verbose_name='ایمیل')

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('profile.html', args=[self.id])
