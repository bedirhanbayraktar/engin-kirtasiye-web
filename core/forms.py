from django import forms
from .models import Order

class SiparisForm(forms.Form):
    adet = forms.IntegerField()
    #spiral = forms.ChoiceField(choices=[('evet', 'Evet'), ('hayir', 'Hayır')], widget=forms.RadioSelect)
    cilt = forms.ChoiceField(choices=[('Zımba', 'Zımba'), ('Sprial', 'Sprial'), ('Karton Kapak', 'Karton Kapak'), ('Bez Cilt', 'Bez Cilt'), ('hiçbiri', 'Hiçbiri')])
    arkalik = forms.ChoiceField(choices=[('tek_tarafli', 'Tek Taraflı'), ('arkali_onlu', 'Arkalı Önlü')], widget=forms.RadioSelect)
    renk = forms.ChoiceField(choices=[('siyah', 'Siyah-Beyaz'), ('renkli', 'Renkli')], widget=forms.RadioSelect)
    dosya = forms.FileField()
    isim_soyisim = forms.CharField(max_length=100, required=True)
    telefon = forms.CharField(max_length=15, required=True)
    notlar = forms.CharField(max_length=200, required=False)


class OrderForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label='İsim')
    phone_number = forms.CharField(max_length=15, required=True, label='Telefon')
    double_sided = forms.ChoiceField(choices=[('Evet', 'Evet'), ('Hayır', 'Hayır')], widget=forms.RadioSelect, label='Arkalı Önlü')
    color_option = forms.ChoiceField(choices=[('Siyah-Beyaz', 'Siyah-Beyaz'), ('Renkli', 'Renkli')], widget=forms.RadioSelect, label='Renk Seçeneği')
    binding_option = forms.ChoiceField(choices=[('Zımba', 'Zımba'), ('Sprial', 'Sprial'), ('Karton Kapak', 'Karton Kapak'), ('Bez Cilt', 'Bez Cilt'), ('hiçbiri', 'Hiçbiri')], label='Ciltleme Seçeneği')
    sayfa_sayisi = forms.IntegerField(label='Sayfa Sayısı', required=True)
    dosya = forms.FileField(label='Dosya')


    class Meta:
        model = Order
        fields = ['name', 'phone_number', 'double_sided', 'color_option', 'binding_option', 'sayfa_sayisi', 'dosya']


