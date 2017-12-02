from django.contrib.auth.models import User, Group
from .models import Mahasiswa, Peminjaman
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MahasiswaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = ('url', 'npm', 'user')

class PeminjamanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peminjaman
        fields = ('mahasiswa', 'nomor_sepeda', 'status_pinjam', 'stasiun_pinjam',
            'stasiun_balik', 'timestamp_pinjam', 'timestamp_balik')
