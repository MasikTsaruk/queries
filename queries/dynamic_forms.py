from django import forms

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
            DynamicRunForm.base_fields[f"{param.name}_min"] = forms.FloatField(
                required=False, label=f"{param.name} (мин)", initial=param.min_number
            )
            DynamicRunForm.base_fields[f"{param.name}_max"] = forms.FloatField(
                required=False, label=f"{param.name} (макс)", initial=param.max_number
            )
        elif param.type == 'date':
            DynamicRunForm.base_fields[f"{param.name}_min"] = forms.DateField(
                required=False, label=f"{param.name} (от)", widget=forms.DateInput(attrs={'type': 'date'}), initial=param.min_date
            )
            DynamicRunForm.base_fields[f"{param.name}_max"] = forms.DateField(
                required=False, label=f"{param.name} (до)", widget=forms.DateInput(attrs={'type': 'date'}), initial=param.max_date
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
