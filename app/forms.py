
from dataclasses import fields
from django import forms

from app.models import AccessRecords, Topic, Webpage

class Topicforms(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class Webpageforms(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'

class AccessRecordforms(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'

