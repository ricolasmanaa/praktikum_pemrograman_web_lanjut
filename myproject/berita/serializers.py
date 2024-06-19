from rest_framework import serializers
from berita.models import Kategori, Artikel
from pengguna.models import Biodata
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class BiodataSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Biodata
        fields = ['id', 'user', 'alamat', 'telepon', 'foto']

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id', 'nama']

class ArtikelSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    kategori = serializers.PrimaryKeyRelatedField(queryset=Kategori.objects.all())

    author_detail = UserSerializer(source='author', read_only=True)
    kategori_detail = KategoriSerializer(source='kategori', read_only=True)
    class Meta:
        model = Artikel
        fields = [
                'id', 'judul', 'isi', 'kategori', 'author', 'kategori_detail', 
                'author_detail', 'thumbnail', 'created_at', 'slug'
                ]
        read_only_fields = ['author_detail', 'kategori_detail']