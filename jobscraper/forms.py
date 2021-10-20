from django import forms

class JobScraperForm(forms.Form):
    job_search = forms.CharField(
        max_length=100,        
        widget=forms.TextInput(attrs={'placeholder': 'Software Developer', 'class': '"col-md-5"'})
    )
    location = forms.CharField(
        max_length=200, 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'San Fransisco', 'class': 'form-control'})
    ) 
    search_size = forms.IntegerField(
        max_value=500,
        widget=forms.TextInput(attrs={'placeholder': 'Search Size', 'class': 'form-control'})
    )
    whitelist = forms.CharField(
        required=False, 
        widget=forms.Textarea(attrs={'style': "width:100%;"}))
    blacklist = forms.CharField(
        required=False, 
        widget=forms.Textarea(attrs={'style': "width:100%;"}))

    def clean(self):
        cleaned_data = super(JobScraperForm, self).clean()
        job_search = cleaned_data.get('job_search')
        location = cleaned_data.get('location')
        whitelist = cleaned_data.get('whitelist')
        blacklist = cleaned_data.get('blacklist')
        search_size = cleaned_data.get('search_size')
        if not job_search and not search_size:
            print("raising validation error!")
            raise forms.ValidationError('Please fill in the required fields')
        
        
        
#fields
#Job search
#Location
#Search size
#whitelist
#blacklist
#common blacklist and whitelist items