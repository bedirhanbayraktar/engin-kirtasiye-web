from django.contrib import admin, messages
from django.utils.html import format_html
from .models import Resim, Fotograf, Siparis, Order

@admin.register(Resim)
class ResimAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'aciklama', 'resim_dosyasi', 'fiyat')

@admin.register(Fotograf)
class FotografAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'fotograf', 'yayinlanma_tarihi')

@admin.register(Siparis)
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

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'double_sided', 'color_option', 'binding_option', 'created_at', 'sayfa_sayisi']
    list_filter = ['double_sided', 'color_option', 'binding_option']
    search_fields = ['name', 'phone_number']
    actions = ['calculate_selected_orders']

    def calculate_selected_orders(self, request, queryset):
        total_price = sum(order.calculate_price() for order in queryset)
        self.message_user(request, f"Seçili siparişlerin toplam fiyatı: {total_price} TL", level=messages.INFO)

    calculate_selected_orders.short_description = "Seçili siparişlerin fiyatını hesapla"

