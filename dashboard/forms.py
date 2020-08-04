from django import forms
    
class ItemForm(forms.Form):
    title = forms.CharField(help_text="이름을 입력하세요")
    contents = forms.CharField(help_text="내용을 입력하세요")

class CommentsForm(forms.Form):
    comment = forms.CharField(help_text="댓글을 입력하세여")