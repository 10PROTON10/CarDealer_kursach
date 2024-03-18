from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand_images/', null=True, blank=True)

    def __str__(self):
        return self.name

# class Car(models.Model):
#     id = models.AutoField(primary_key=True)
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     model = models.CharField(max_length=100)
#     year = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     engine = models.CharField(max_length=100)
#     image = models.CharField(max_length=200, null=True, blank=True)
#
#     def __str__(self):
#         return f"{self.year} {self.brand} {self.model}"

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.PositiveIntegerField(null=True, blank=True)
    engine = models.CharField(max_length=100)
    engine_volume = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    engine_power = models.PositiveIntegerField(null=True, blank=True)
    transmission = models.CharField(max_length=100, null=True, blank=True)
    gears = models.PositiveIntegerField(null=True, blank=True)
    drive = models.CharField(max_length=20, null=True, blank=True)
    fuel_consumption = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    body_type = models.CharField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)


class Customer(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    registration_date = models.DateField(default=timezone.now)
    city = models.CharField(max_length=100, default='')
    contact_phone = models.CharField(max_length=20, default='')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    age = models.PositiveIntegerField(default=0)
    address = models.TextField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    ORDER_STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='processing')

    def __str__(self):
        return f"Order {self.id} - {self.customer}"

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    review_text = models.TextField()

    def __str__(self):
        return f"Review by {self.author} for {self.car}"

class CarAccessory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='accessories/', null=True, blank=True)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    is_selected_for_comparison = models.BooleanField(default=False)