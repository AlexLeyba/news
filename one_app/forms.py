from django import forms
from one_app.models import Comment


class CommentForm(forms.ModelForm):
    """Форма коммегтариев"""

    class Meta:
        model = Comment
        fields = ("text",)
