from django.contrib import admin

# Register your models here.

from .models import Penulis, Buku, Peminjaman

@admin.register(Penulis)
class PenulisAdmin(admin.ModelAdmin):
    list_display = ('nama', 'negara_asal')

@admin.register(Buku)
class BukuAdmin(admin.ModelAdmin):
    list_display = ('judul', 'isbn', 'tahun_terbit', 'penulis')
    list_filter = ('penulis',)

@admin.register(Peminjaman)
class PeminjamanAdmin(admin.ModelAdmin):
    list_display = ('buku', 'peminjam', 'tanggal_peminjaman', 'tanggal_pengembalian')
    list_filter = ('buku', 'peminjam')
    search_fields = ('buku__judul', 'peminjam')
