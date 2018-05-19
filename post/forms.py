from django import forms

from .models import Post, Section, Comment


class PostForm(forms.ModelForm):
    # article_title = forms.CharField(max_length=100)
    # article_section = forms.ModelChoiceField(queryset=Section.objects.all(), empty_label=None)
    # article_content = forms.TextField()
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['post_title'].widget.attrs = {'class': 'form-control form-control-lg',
                                                     'placeholder': "Заголовок*"}
        self.fields['post_title'].label = ''

        self.fields['post_section'].widget.attrs = {'class': 'custom-select'}
        self.fields['post_section'].label = 'Выберите Категорию*'

        self.fields['post_content'].widget.attrs = {'class': 'form-control rounded-0', 'rows': "10",
                                               'placeholder': "Ваша Заявка*"}
        self.fields['post_content'].label = ''

    class Meta:
        model = Post
        fields = ['post_title', 'post_section', 'post_photo', 'post_content']


class CommentForm(forms.Form):
    comment_area = forms.CharField(
        label="",
        widget=forms.Textarea
    )