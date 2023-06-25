from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Resim, Fotograf, Siparis
from .views import home, about, products, contact


class ViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        # Test verilerini oluşturmak için örnek nesneler yaratılıyor
        self.resim = Resim.objects.create(baslik='Test Resim Başlık')
        self.fotograf = Fotograf.objects.create(baslik='Test Fotoğraf Başlık')
    
    def test_home_view(self):
        url = reverse('home')
        request = self.factory.get(url)
        response = home(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Anasayfa')
        self.assertQuerysetEqual(response.context['resimler'], [repr(self.resim)])
        self.assertQuerysetEqual(response.context['fotograf_listesi'], [repr(self.fotograf)])
    
    def test_about_view(self):
        url = reverse('about')
        request = self.factory.get(url)
        response = about(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hakkında')
    
    def test_products_view(self):
        url = reverse('products')
        request = self.factory.get(url)
        response = products(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ürünler')
    
    def test_contact_view(self):
        url = reverse('contact')
        request = self.factory.get(url)
        response = contact(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'İletişim')


# Yukarıdaki testleri çalıştırmak için aşağıdaki kodu kullanabilirsiniz
# python manage.py test

