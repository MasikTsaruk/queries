from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


def build_dynamic_run_form(parameters):
    class DynamicRunForm(forms.Form):
        pass

    for param in parameters:
        if param.type == 'string':
            DynamicRunForm.base_fields[param.name] = forms.CharField(
                required=param.required,
                label=param.name,
                widget=forms.TextInput(attrs={'placeholder': f'Type value for {param.name}'})
            )
        elif param.type == 'number':
            validators = []
            if param.min_number is not None:
                validators.append(MinValueValidator(param.min_number))
            if param.max_number is not None:
                validators.append(MaxValueValidator(param.max_number))
            
            DynamicRunForm.base_fields[param.name] = forms.FloatField(
                required=param.required,
                label=param.name,
                validators=validators,
                widget=forms.NumberInput(attrs={
                    'min': param.min_number,
                    'max': param.max_number
                })
            )
        elif param.type == 'date':
            attrs = {'type': 'date'}
            if param.min_date:
                attrs['min'] = param.min_date.strftime('%Y-%m-%d')
            if param.max_date:
                attrs['max'] = param.max_date.strftime('%Y-%m-%d')

            DynamicRunForm.base_fields[param.name] = forms.DateField(
                required=param.required,
                label=param.name,
                widget=forms.DateInput(attrs=attrs),
            )

            DynamicRunForm.base_fields[param.name] = forms.DateField(
                required=param.required,
                label=param.name,
                widget=forms.DateInput(attrs=attrs),
                initial=param.min_date  
            )
        elif param.type == 'select':
            choices = [(v, v) for v in param.multiselect_allowed_values()]
            DynamicRunForm.base_fields[param.name] = forms.ChoiceField(
                choices=choices,
                required=param.required,
                label=param.name
            )
        elif param.type == 'multiselect':
            choices = [(v, v) for v in param.multiselect_allowed_values()]
            DynamicRunForm.base_fields[param.name] = forms.MultipleChoiceField(
                choices=choices,
                required=param.required,
                label=param.name
            )
    return DynamicRunForm
