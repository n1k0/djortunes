from django.forms import ModelForm
from djortunes.fortunes.models import Comment, Fortune

class CommentForm(ModelForm):
    class Meta:
        model = Comment

class FortuneForm(ModelForm):
    class Meta:
        model = Fortune

class PublicCommentForm(CommentForm):
    class Meta(CommentForm.Meta):
        exclude = ['fortune', 'pub_date']

class PublicFortuneForm(FortuneForm):
    class Meta(FortuneForm.Meta):
        exclude = ['pub_date', 'votes']

