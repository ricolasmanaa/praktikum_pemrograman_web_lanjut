from django.contrib import admin
from django.urls import path, include

#untuk menampilkan gambar yang sudah diupload pada folder media
from django.conf import settings
from django.conf.urls.static import static

from myproject.views import home, detail_artikel, about, contact
from myproject.authentikasi import akun_login, akun_registrasi, akun_logout

from berita.api import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('dashboard/', include("berita.urls")),
    path('artikel/<slug:slug>', detail_artikel, name='detail_artikel'),

    path('about', about, name='about'),
    path('contact', contact, name='contact'),

    path('authentikasi/login', akun_login, name='akun_login'),
    path('authentikasi/registrasi', akun_registrasi, name='akun_registrasi'),
    path('authentikasi/logout', akun_logout, name='akun_logout'),
    
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('api/author/list', api_author_list),
    path('api/author/detail/<int:id_author>', api_author_detail),

    path('api/kategori/list', api_kategori_list),
    path('api/kategori/add', api_kategori_add),
    path('api/kategori/detail/<int:id_kategori>', api_kategori_detail),

    path('api/artikel/list', api_artikel_list),
    path('api/artikel/add', api_artikel_add),
    path('api/artikel/detail/<int:id_artikel>', api_artikel_detail),

]

#untuk menampilkan gambar yang sudah diupload pada folder media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
                          