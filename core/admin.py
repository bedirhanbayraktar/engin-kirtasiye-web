from django.contrib import admin, messages
from .models import Resim, Fotograf, Siparis
from django.utils.html import format_html


@admin.register(Resim)
class ResimAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'aciklama', 'resim_dosyasi', 'fiyat')

@admin.register(Fotograf)
class FotografAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'fotograf', 'yayinlanma_tarihi')


class SiparisAdmin(admin.ModelAdmin):
    list_display = ['resim', 'adet', 'spiral', 'arkalik', 'renk', 'dosya', 'isim_soyisim', 'telefon', 'notlar']
    list_filter = ['resim', 'spiral', 'arkalik', 'renk']
    search_fields = ['resim__baslik', 'dosya']

    def save_model(self, request, obj, form, change):
        obj.save()
    
        # Yeni bir bildirim göster
        message = format_html('Yeni bir sipariş verildi: <a href="{}">{}</a>', obj.resim.get_absolute_url(), obj.resim.baslik)
        self.message_user(request, message, level=messages.SUCCESS)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(isim_soyisim=None, telefon=None, notlar=None)


admin.site.register(Siparis, SiparisAdmin)
