from django.forms import ModelForm
from django_fortunes.models import Fortune

class FortuneForm(ModelForm):
    class Meta:
        model = Fortune

class PublicFortuneForm(FortuneForm):
    class Meta(FortuneForm.Meta):
        exclude = ('pub_date', 'votes', 'slug',)