from django import forms
from one_app.models import Comment


class CommentForm(forms.ModelForm):
    """Форма коммегтариев"""

    class Meta:
        model = Comment
        fields = ("text",)


class Search(forms.Form):
    search = forms.CharField(label="Поиск", max_length=200)