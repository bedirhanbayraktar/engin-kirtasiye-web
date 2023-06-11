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

    