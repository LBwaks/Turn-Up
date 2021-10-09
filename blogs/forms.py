from django import forms
from .models import Blog_Comment
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Blog_Comment
        fields= ('body',)

        widgets = {
           
             'body': forms.CharField(widget=CKEditorWidget()),
        }