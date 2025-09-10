from django import forms
from .models import Query, QueryParameter
from crispy_forms.helper import FormHelper


class QueryForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Query
        fields = ['name', 'password', 'description', 'recipient', 'template', 'db_dsn']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'template': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter SQL query here...'}),
            'db_dsn': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Example: postgresql://user:pass@host:port/dbname'}),
            'password': forms.PasswordInput
        }

        labels = {
            'name': 'Query Name',
            'description': 'Description (optional)',
            'recipient': 'Recipient (e.g. email or service)',
            'template': 'SQL Query',
            'db_dsn': 'Database DSN',
        }
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipient'].required = False
        self.fields['recipient'].label_suffix = ""
        self.helper = FormHelper()
        self.helper.render_required_fields = False

class QueryEditForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['name', 'description', 'recipient', 'template', 'db_dsn']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'template': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter SQL query here...'}),
            'db_dsn': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Example: postgresql://user:pass@host:port/dbname'}),
        }

        labels = {
            'name': 'Query Name',
            'description': 'Description (optional)',
            'recipient': 'Recipient (e.g. email or service)',
            'template': 'SQL Query',
            'db_dsn': 'Database DSN',
        }

class QueryChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        label='Type here your old password',
        widget=forms.PasswordInput,
        required=False
    )
    new_password = forms.CharField(
        label='Type here your new password',
        widget=forms.PasswordInput,
        required=False
    )

class QueryParameterForm(forms.ModelForm):
    class Meta:
        model = QueryParameter
        fields = [
            'name', 'type',
            'min_number', 'max_number',
            'min_date', 'max_date',
            'allowed_values', 'required'
        ]
        widgets = {
            'min_date': forms.DateInput(attrs={'type': 'date'}),
            'max_date': forms.DateInput(attrs={'type': 'date'}),
            'allowed_values': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter values separated by commas'}),
        }



