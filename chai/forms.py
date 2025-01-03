from django  import forms
from .models import ChaiVarity

class ChaiVarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=ChaiVarity.objects.all(),label="Select chai variety")

    # chai_varity = forms.IntegerField()