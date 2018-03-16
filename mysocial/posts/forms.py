from django import forms
from .models import Post
from groups.models import Group

class PostForm(forms.ModelForm):
    class Meta:
        fields = ("message", 'group')
        model = Post

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields['group'].widget.attrs.update({'class':'browser-default'})
        if user is not None:
            self.fields['group'].queryset = (
                Group.objects.filter(
                    pk__in=user.groups.values_list("group__pk")
                )
            )
