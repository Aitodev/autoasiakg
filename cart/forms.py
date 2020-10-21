from django import forms

PRODUCT_QUANTITY_CHOISES = [(i, str(i)) for i in range(1, 100)]


class CartAddProductForm(forms.Form):
    quantity = forms.CharField(required=False, initial=1, widget=forms.HiddenInput)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    
class OrderSendForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    mail = forms.CharField(required=False)
