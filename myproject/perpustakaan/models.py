from django.db import models

# Create your models here.

class Penulis(models.Model):
    nama = models.CharField(max_length=100)
    negara_asal = models.CharField(max_length=100)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = '1. Penulis'

class Buku(models.Model):
    judul = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    tahun_terbit = models.IntegerField()
    penulis = models.ForeignKey(Penulis, on_delete=models.CASCADE, related_name='buku')

    def __str__(self):
        return self.judul

    class Meta:
        verbose_name_plural = '2. Buku'

class Peminjaman(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    peminjam = models.CharField(max_length=100)
    tanggal_peminjaman = models.DateField()
    tanggal_pengembalian = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.buku.judul} dipinjam oleh {self.peminjam}"

    class Meta:
        verbose_name_plural = '3. Peminjaman'