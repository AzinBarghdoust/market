from django.contrib.auth.hashers import make_password
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
    id = models.PositiveBigIntegerField(primary_key=True, editable=False)
    username = None
    phone = models.CharField(max_length=11, unique=True, verbose_name='شماره موبایل', blank=False,
                             help_text='Enter 11 digits phone number')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            last_pk = CustomUser.objects.values_list('id', flat=True).last()
            last_pk = int(str(last_pk)[:4]) if last_pk else 1000
            phone_ext = self.phone[1:4]
            pk = int(f'{last_pk + 1}{phone_ext}')
            self.id = pk
        return super(CustomUser, self).save(force_insert, force_update, using, update_fields)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.crew_password = make_password(self.password)
        super(CustomUser, self).save(*args, **kwargs)


class PhoneOTP(models.Model):
    phone = models.CharField(max_length=11, null=True)
    otp = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    Man = 1
    Woman = 2
    STATUS_CHOICES = ((Man, 'مرد'), (Woman, "زن"))
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, verbose_name='نام', blank=True, null=True)
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی', blank=True, null=True)
    gender = models.IntegerField(choices=STATUS_CHOICES, verbose_name='جنسیت', blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, unique=True, null=True, verbose_name='ایمیل')
    city = models.CharField(max_length=20, blank=True, verbose_name='استان')

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('profile.html', args=[self.id])
