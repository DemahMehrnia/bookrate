from  django import forms

class add_blog(forms.Form):
    title = forms.CharField(
        label='عنوان',
        max_length=50,
        error_messages={
            'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
            'max_length': 'نام و نام خانوادگی نمی تواند بیشتر از 50 کاراکتر باشد'
        }
    )
    image = forms.ImageField(label='عکس')
    shortdes = forms.CharField(
        label='متن کوتاه',
        widget=forms.Textarea

    )

    contet = forms.CharField(
        label='متن مقاله',
        widget=forms.Textarea


    )
