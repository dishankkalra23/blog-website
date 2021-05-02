from django import forms
from .models import Post, Category

# choice = Category.objects.all().values_list('name', 'name')

choice_list = [('education', 'Education'), ('fashion', 'Fashion'), ('lifestyle', 'Lifestyle'),
               ('spirituality', 'Spirituality'), ('food', 'Food')]

choice_list_1 = (
    ('True', True),
    ('False', False)
)

type_1 = (
    ('Professional', 'Professional'),
    ('Student', 'Student'),
    ('Freelancer', 'Freelancer'),
)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'author', 'category', 'read_time', 'float_field', 'reading_type_professional', 'writer_type',
            'body',
            'header_image')

        # choice_list_1 = [('True', True), ('False', False)]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(
                attrs={'class': 'form-control', 'value': '', 'id': 'dish'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'reading_type_professional': forms.RadioSelect(choices=choice_list_1),
            'writer_type': forms.CheckboxSelectMultiple(choices=type_1),
            'read_time': forms.NumberInput(),
            'float_field': forms.NumberInput(),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
