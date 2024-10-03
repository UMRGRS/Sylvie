from django import forms

from ..models import Company

from ..utils.cloudinary_images import upload_image, replace_image

class CompanyForm(forms.ModelForm):
    logo = forms.ImageField(widget=forms.FileInput, required=False)
    
    class Meta:
        model = Company
        fields = [ 'name', 'email', 'phone', 'logo']
    
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        
        super().__init__(*args, **kwargs)
        
        if instance and instance.logo_url:
            self.fields['logo'].help_text = f'Current: <a href="{instance.logo_url}">{instance.logo_url}</a>'
        
    def save(self, commit=True):
        if not self.instance.pk and self.cleaned_data['logo']:
            upload_data = upload_image(self.cleaned_data['logo'])
        elif self.instance.logo_url and self.cleaned_data['logo']:
            upload_data = replace_image(self.instance.logo_public_id, self.cleaned_data['logo'])
        elif self.cleaned_data['logo']:
            upload_data = upload_image(self.cleaned_data['logo'])
        
        if upload_data:
            self.instance.logo_url = upload_data['secure_url']
            self.instance.logo_public_id = upload_data['public_id']
        
        return super().save(commit)
        