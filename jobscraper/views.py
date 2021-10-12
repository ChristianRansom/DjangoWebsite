from django.shortcuts import render, redirect
from jobscraper.forms import JobScraperForm
from django.urls import reverse


# Create your views here.
def job_scraper(request):
    if request.method == "GET":
        return render(
            request, 
            'job_scraper/job_scraper.html', 
            {"form": JobScraperForm}
        )
    elif request.method == "POST":
        form = JobScraperForm(request.POST)
        if form.is_valid():        
            job_search = form.cleaned_data['job_search']
            location = form.cleaned_data['location']  
            whitelist = form.cleaned_data['whitelist']
            blacklist = form.cleaned_data['blacklist']
            search_size = form.cleaned_data['search_size']
            print("We got something: " + job_search)
            
        return render(
            request, 
            'job_scraper/job_scraper.html', 
            {"form": form}
        )



