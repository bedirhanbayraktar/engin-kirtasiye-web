from django.shortcuts import render, get_object_or_404, redirect
from .models import Resim, Fotograf, Siparis
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from .forms import SiparisForm, OrderForm


def home(request):
    resimler = Resim.objects.all()
    fotograf_listesi = Fotograf.objects.order_by('-yayinlanma_tarihi')
    return render(request, 'home.html', {'resimler': resimler, 'fotograf_listesi': fotograf_listesi})

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def contact(request):
    return render(request, 'contact.html')


def resim_detay(request, id):
    resim = get_object_or_404(Resim, id=id)
    
    if request.method == 'POST':
        form = SiparisForm(request.POST, request.FILES)
        if form.is_valid():
            adet = form.cleaned_data['adet']
            spiral = form.cleaned_data['spiral']  
            arkalik = form.cleaned_data['arkalik']
            renk = form.cleaned_data['renk']
            dosya = form.cleaned_data['dosya']
            isim_soyisim = form.cleaned_data['isim_soyisim']
            telefon = form.cleaned_data['telefon']
            notlar = form.cleaned_data['notlar']

            # Yeni bir sipariş öğesi oluşturma
            siparis = Siparis(
                resim=resim,
                adet=adet,
                spiral=spiral,
                arkalik=arkalik,
                renk=renk,
                dosya=dosya
            )

            if isim_soyisim and telefon:
                siparis.isim_soyisim = isim_soyisim
                siparis.telefon = telefon
    
            if notlar:
                siparis.notlar = notlar
                siparis.save()
            
            # Yeni bir girdi oluşturarak admin paneline bildirim gönderme
            content_type = ContentType.objects.get_for_model(siparis)
            '''
            LogEntry.objects.log_action(
                user_id=None,
                content_type_id=content_type.pk,
                object_id=siparis.pk,
                object_repr="Sipariş Verildi - {}".format(resim.baslik),
                change_message="Adet: {}, Spiral: {}, Arkalık: {}, Renk: {}, Dosya: {}".format(adet, spiral, arkalik, renk, dosya.name),
                action_flag=ADDITION,
            )
            '''
            return redirect('home')
    else:
        form = SiparisForm()
        
    context = {'resim': resim, 'form': form}
    return render(request, 'resim_detay.html', context)


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()  # Siparişi kaydet
            calculated_price = order.calculate_price()  # Fiyatı hesapla
            return render(request, 'order_confirmation.html', {'order': order, 'calculated_price': calculated_price})
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})

