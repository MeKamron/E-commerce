from django import forms 

class CartAddProductForm(forms.Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
