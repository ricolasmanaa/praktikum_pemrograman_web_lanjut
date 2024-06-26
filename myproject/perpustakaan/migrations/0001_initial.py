# Generated by Django 5.0.3 on 2024-03-25 00:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=20, unique=True)),
                ('tahun_terbit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Penulis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('negara_asal', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Peminjaman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peminjam', models.CharField(max_length=100)),
                ('tanggal_peminjaman', models.DateField()),
                ('tanggal_pengembalian', models.DateField(blank=True, null=True)),
                ('buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.buku')),
            ],
        ),
        migrations.AddField(
            model_name='buku',
            name='penulis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buku', to='perpustakaan.penulis'),
        ),
    ]
