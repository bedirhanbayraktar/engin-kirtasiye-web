from django.db import models
from PIL import Image

class Resim(models.Model):
    baslik = models.CharField(max_length=100)
    aciklama = models.TextField()
    resim_dosyasi = models.ImageField(upload_to='resimler/')
    fiyat = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.baslik


class Fotograf(models.Model):
    baslik = models.CharField(max_length=100)
    fotograf = models.ImageField(upload_to='fotograflar/')
    yayinlanma_tarihi = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.baslik

    def save(self, *args, **kwargs):
        super(Fotograf, self).save(*args, **kwargs)
        img = Image.open(self.fotograf.path)

        # Fotoğraf boyutunu kontrol et ve gerekirse boyutlandır
        if img.height > 1024 or img.width > 1024:
            output_size = (1024, 1024)
            img.thumbnail(output_size)
            img.save(self.fotograf.path)

    class Meta:
        verbose_name_plural = 'Fotograflar'


class Siparis(models.Model):
    resim = models.ForeignKey(Resim, on_delete=models.CASCADE)
    adet = models.IntegerField()
    spiral = models.CharField(max_length=5)
    arkalik = models.CharField(max_length=20)
    renk = models.CharField(max_length=20)
    dosya = models.FileField(upload_to='siparisler/')
    isim_soyisim = models.CharField(max_length=100)
    telefon = models.CharField(max_length=10)
    notlar = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "Sipariş #{} - {}".format(self.id, self.resim.baslik)

    

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    double_sided = models.CharField(max_length=20)
    color_option = models.CharField(max_length=20)
    binding_option = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    sayfa_sayisi = models.IntegerField(null=True)


    def calculate_price(self):
        price = 0

        if self.double_sided == 'Evet':
            price += 1 * self.sayfa_sayisi # Arklı-önlü seçeneği için 1 TL ekleniyor
        else:
            price += 2 * self.sayfa_sayisi # Tek taraflıysa sayfası 2 TL.

        if self.color_option == 'Renkli':
            price += 2 * self.sayfa_sayisi # Renkli çıktı seçeneği için 1 TL ekleniyor

        if self.color_option == 'Siyah-Beyaz':
            price += 0  # Renkli çıktı seçeneği için 1 TL ekleniyor

        # Ciltleme seçeneklerine göre fiyat hesaplanıyor
        if self.binding_option == 'Zımba':
            price += 0
        elif self.binding_option == 'Sprial':
            price += 25
        elif self.binding_option == 'Karton Kapak':
            price += 35
        elif self.binding_option == 'Bez Cilt':
            price += 160
         
        return price