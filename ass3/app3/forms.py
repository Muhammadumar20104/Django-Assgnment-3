from django.forms import ModelForm
from .models import Details

class Detailform(ModelForm):
    class Meta:
        model = Details
        fields = '__all__'