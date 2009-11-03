from django.forms import ModelForm
from djortunes.fortunes.models import Fortune, Comment

class FortuneForm(ModelForm):
    class Meta:
        model = Fortune

class CommentForm(ModelForm):
    class Meta:
        model = Comment

class PublicFortuneForm(FortuneForm):
    class Meta(FortuneForm.Meta):
        exclude = ['pub_date', 'votes']
