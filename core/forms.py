from django import forms

class SiparisForm(forms.Form):
    adet = forms.IntegerField()
    spiral = forms.ChoiceField(choices=[('evet', 'Evet'), ('hayir', 'Hayır')], widget=forms.RadioSelect)
    arkalik = forms.ChoiceField(choices=[('tek_tarafli', 'Tek Taraflı'), ('arkali_onlu', 'Arkalı Önlü')], widget=forms.RadioSelect)
    renk = forms.ChoiceField(choices=[('siyah', 'Siyah-Beyaz'), ('renkli', 'Renkli')], widget=forms.RadioSelect)
    dosya = forms.FileField()
    isim_soyisim = forms.CharField(max_length=100, required=True)
    telefon = forms.CharField(max_length=15, required=True)
    notlar = forms.CharField(max_length=200, required=False)