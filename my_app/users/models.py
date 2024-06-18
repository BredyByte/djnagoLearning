from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	image = models.ImageField(upload_to='user_images', blank=True, null=True, verbose_name='La foto de usuario')
	phone_number = models.CharField(max_length=10, blank=True, null=True)

	class Meta:
		db_table = 'user'
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'
		ordering = ("id",)

	def __str__(self):
		return self.username

