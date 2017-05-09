from django import forms
from dashboard.models import user_info
from webstats.models import Support

class imageForm(forms.ModelForm):
    class Meta:
        model = user_info
        fields = [
            'user_image',
        ]

class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = [
            'priority',
            'subj',
            'msg'
        ]
