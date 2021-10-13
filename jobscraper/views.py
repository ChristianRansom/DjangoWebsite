from django.shortcuts import render
from jobscraper.forms import JobScraperForm
from . import job_scraper as scrapper_script

# Create your views here.
def job_scraper(request):
    if request.method == "GET":
        return render(
            request, 
            'job_scraper/job_scraper.html', 
            {"form": JobScraperForm,
            }
        )
    elif request.method == "POST":
        form = JobScraperForm(request.POST)
        if form.is_valid():        
            job_search = form.cleaned_data['job_search']
            location = form.cleaned_data['location']  
            whitelist = form.cleaned_data['whitelist']
            blacklist = form.cleaned_data['blacklist']
            search_size = form.cleaned_data['search_size']
            
            scraped = scrapper_script.scrape_jobs(job_search, whitelist, blacklist, search_size, location)
            #scraped_text = [i for i in scraped]
            #print("scraped text: " + scraped)
            
            scraped = {"scraped": scraped}

        
            return render(
                request, 
                'job_scraper/job_scraper.html', 
                {"form": form,
                 "scraped": scraped,
                 }
            )
        else:
            return render(
                request, 
                'job_scraper/job_scraper.html', 
                {"form": form}
        )
    



