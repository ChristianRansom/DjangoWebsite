from django import forms

class JobScraperForm(forms.Form):
    job_search = forms.CharField(
        max_length=100,        
        help_text='This field is required'
    )
    search_size = forms.IntegerField(
        max_value=500,
        help_text='This field is required'
    )
    location = forms.CharField(max_length=100, required=False) 
    whitelist = forms.CharField(widget=forms.Textarea(), required=False)
    blacklist = forms.CharField(widget=forms.Textarea(), required=False)

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