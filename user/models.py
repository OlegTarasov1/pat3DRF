from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.text import slugify

class NewUser(AbstractUser):
    email = models.EmailField(blank = False, null = False, max_length=100, unique = True)
    first_name = models.CharField(blank = False, null = False, max_length = 100)
    last_name = models.CharField(blank = False, null = False, max_length = 100)
    slug = models.SlugField(blank = False, null = False, unique = True)
    birth_date = models.DateField(null = True, blank = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)


class Balance(models.Model):
    balance = models.DecimalField(decimal_places=2, max_digits=10, default = 100.00)
    owner = models.OneToOneField(get_user_model(), related_name = 'balance', on_delete=models.CASCADE)