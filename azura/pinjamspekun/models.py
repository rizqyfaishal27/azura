from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Mahasiswa(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	npm = models.CharField(max_length=10)

	def __str__(self):
		return self.npm

class Peminjaman(models.Model):
	mahasiswa = models.OneToOneField(Mahasiswa, on_delete=models.CASCADE)
	nomor_sepeda = models.CharField(max_length=4)
	status_pinjam = models.BooleanField(default=True)
	stasiun_pinjam = models.CharField(max_length=255)
	stasiun_balik = models.CharField(max_length=255, default=None)
	timestamp_pinjam = models.DateTimeField(auto_now_add=True)
	timestamp_balik = models.DateTimeField(auto_now=True)

	def __str__(self):
		return mahasiswa.user.full_name
