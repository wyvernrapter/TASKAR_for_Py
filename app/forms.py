from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re
from .models import Item
import requests
import json
from django.conf import settings





class ItemForm(forms.ModelForm):
    postcode = forms.CharField(label='郵便番号', max_length=7, widget=forms.TextInput(attrs={'onblur': 'fetchAddress()', 'onkeypress': 'if(event.keyCode == 13) fetchAddress()'}))
    address = forms.CharField(label='住所', required=False)

    phone_regex = RegexValidator(
        regex=r'^0\d{1,4}-\d{1,4}-\d{4}$',
        message="正しい電話番号を入力してください。"
    )
    section = forms.ChoiceField(choices=(
        ('管理本部', '管理本部'),
        ('財務部', '財務部'),
        ('法務部', '法務部'),
        ('人事部', '人事部'),
        ('営業一部', '営業一部'),
        ('営業二部', '営業二部'),
        ('IT一部', 'IT一部'),
        ('IT二部', 'IT二部'),
        ('広報部', '広報部')
    ), widget=forms.Select(attrs={'class': 'form-control'}), label='部署')

    rank = forms.ChoiceField(choices=(
        ('代表取締役社長', '代表取締役社長'),
        ('常務取締役', '常務取締役'),
        ('専務取締役', '専務取締役'),
        ('本部長', '本部長'),
        ('部長', '部長'),
        ('次長', '次長'),
        ('課長', '課長'),
        ('課長代理', '課長代理'),
        ('係長', '係長'),
        ('社員', '社員')
    ), widget=forms.Select(attrs={'class': 'form-control'}), label='役職', initial='社員')

    Lessoning = forms.MultipleChoiceField(choices=(
        ('', 'なし'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('JavaScript/jQuery', 'JavaScript/jQuery'),
        ('PHP', 'PHP'),
        ('Python', 'Python'),
        ('SQL(MySQL)', 'SQL(MySQL)'),
        ('Java', 'Java'),
        ('C', 'C'),
        ('C#', 'C#'),
        ('C++', 'C++'),
        ('Ruby', 'Ruby'),
        ('VBA', 'VBA'),
        ('GAS', 'GAS'),
    ), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}), label='勉強中プログラミング言語', required=False)

    Lessoning_F = forms.MultipleChoiceField(choices=(
        ('', 'なし'),
        ('Laravel', 'Laravel'),
        ('Ruby on rails', 'Ruby on rails'),
        ('Django', 'Django'),
        ('React', 'React'),
        ('Next.js', 'Next.js'),
        ('Vue.js', 'Vue.js'),
        ('Angular', 'Angular'),
    ), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}), label='勉強中Webフレームワーク', required=False)

    Tecnic = forms.MultipleChoiceField(choices=(
        ('', 'なし'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('JavaScript/jQuery', 'JavaScript/jQuery'),
        ('PHP', 'PHP'),
        ('Python', 'Python'),
        ('SQL(MySQL)', 'SQL(MySQL)'),
        ('Java', 'Java'),
        ('C', 'C'),
        ('C#', 'C#'),
        ('C++', 'C++'),
        ('Ruby', 'Ruby'),
        ('VBA', 'VBA'),
        ('GAS', 'GAS'),

    ), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}), label='使用可能プログラミング言語', required=False)

    Tecnic_F = forms.MultipleChoiceField(choices=(
        ('', 'なし'),
        ('Laravel', 'Laravel'),
        ('Ruby on rails', 'Ruby on rails'),
        ('Django', 'Django'),
        ('React', 'React'),
        ('Next.js', 'Next.js'),
        ('Vue.js', 'Vue.js'),
        ('Angular', 'Angular'),
    ), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}), label='使用可能Webフレームワーク', required=False)

    Experience = forms.MultipleChoiceField(choices=(
        ('', 'なし'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('JavaScript/jQuery', 'JavaScript/jQuery'),
        ('PHP', 'PHP'),
        ('Python', 'Python'),
        ('SQL(MySQL)', 'SQL(MySQL)'),
        ('Java', 'Java'),
        ('C', 'C'),
        ('C#', 'C#'),
        ('C++', 'C++'),
        ('Ruby', 'Ruby'),
        ('VBA', 'VBA'),
        ('GAS', 'GAS'),
    ), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}), label='業務経験プログラミング言語', required=False)

    Experience_F = forms.MultipleChoiceField(choices=(
        ('', 'なし'),
        ('Laravel', 'Laravel'),
        ('Ruby on rails', 'Ruby on rails'),
        ('Django', 'Django'),
        ('React', 'React'),
        ('Next.js', 'Next.js'),
        ('Vue.js', 'Vue.js'),
        ('Angular', 'Angular'),
    ), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}), label='業務経験Webフレームワーク', required=False)

    officePC_L = forms.MultipleChoiceField(choices=(
        ('', 'なし'),
        ('Excel', 'Excel'),
        ('Word', 'Word'),
        ('PowerPoint', 'PowerPoint'),
        ('Access', 'Access'),
        ('Google SpreadSheet', 'Google SpreadSheet'),
        ('GoogleDocs', 'GoogleDocs'),

    ), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}), label='勉強中アプリケーション', required=False)

    officePC_T = forms.MultipleChoiceField(choices=(
        ('', 'なし'),
        ('Excel', 'Excel'),
        ('Word', 'Word'),
        ('PowerPoint', 'PowerPoint'),
        ('Access', 'Access'),
        ('Google SpreadSheet', 'Google SpreadSheet'),
        ('GoogleDocs', 'GoogleDocs'),

    ), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}), label='使用可能アプリケーション', required=False)

    officePC_E = forms.MultipleChoiceField(choices=(
        ('', 'なし'),
        ('Excel', 'Excel'),
        ('Word', 'Word'),
        ('PowerPoint', 'PowerPoint'),
        ('Access', 'Access'),
        ('Google SpreadSheet', 'Google SpreadSheet'),
        ('GoogleDocs', 'GoogleDocs'),

    ), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}), label='業務経験アプリケーション', required=False)

    class Meta:
        model = Item
        fields = ('employee_number', 'name', 'age', 'section', 'rank', 'email_add', 'phone', 'postcode', 'address', 'station1', 'sex', 'memo', 'Lessoning' , 'Lessoning_F', 'Tecnic', 'Tecnic_F', 'Experience', 'Experience_F', 'officePC_L', 'officePC_T', 'officePC_E')
        widgets = {
            'employee_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '記入例：12345'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email_add': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '記入例：xxx@example.com'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'station1': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.RadioSelect(choices=(('male', '男'), ('female', '女'))),
            'memo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '記入例：自由記述欄'}),
        }
        labels = {
            'email_add': 'Eメールアドレス',
            'phone': '電話番号',
            'postcode': '郵便番号',
            'address': '住所',
        }
        error_messages = {
            'sex': {'required': '性別を選択してください。'},
        }


    def clean_age(self):
        age = str(self.cleaned_data['age'])
        if int(age) < 18 or int(age) > 70:
            raise ValidationError('年齢は18歳から70歳までの範囲で入力してください。')
        return age

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            phone = phone.replace('-', '')
            if not re.match(r'^0\d{1,4}\d{1,4}\d{4}$', phone):
                raise forms.ValidationError("正しい電話番号を入力してください。")
        return phone

    def clean(self):
        cleaned_data = super().clean()
        postcode = cleaned_data.get('postcode')

        if not postcode:
            raise forms.ValidationError('郵便番号を入力してください。')

        url = "https://zipcloud.ibsnet.co.jp/api/search"
        params = {"zipcode": postcode}
        res = requests.get(url, params)
        data = json.loads(res.text)

        if data["status"] == 200:
            address1 = data["results"][0]["address1"]
            address2 = data["results"][0]["address2"]
            address3 = data["results"][0]["address3"]
            address = f"{address1}{address2}{address3}"
            self.cleaned_data['address'] = address
        else:
            raise forms.ValidationError('有効な郵便番号を入力してください。')

        return cleaned_data
    #
    # # 住所が存在しない場合のバリデーションチェック
    # class YourForm(forms.ModelForm):
    #     API_KEY = 'AIzaSyCqiYNAANuvDuzEBy7R4Fr1svipbfpxc-Y'
    #
    #     def clean_address(self):
    #         address = self.cleaned_data.get('address')
    #         if address:
    #             url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={self.API_KEY}'
    #             response = requests.get(url)
    #             if response.ok:
    #                 json_data = response.json()
    #                 if json_data['status'] == 'OK':
    #                     return address
    #             raise forms.ValidationError('存在する住所を入力してください。')
    #         else:
    #             raise forms.ValidationError('住所を入力してください。')