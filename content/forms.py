from django import forms
from django.core.validators import FileExtensionValidator

class AddPostForm(forms.Form):
    caption = forms.CharField(max_length=2048, required=False, widget=forms.Textarea)
    caption.widget.attrs.update({"class":"form-control"})


    media = forms.ImageField(
        label="Select from your computer",
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif'])],
        required=True
    )
    media.widget.attrs.update({'class':'btn btn-primary d-none', 'id': 'post-media', 'multiple': True})


