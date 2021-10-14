from django.shortcuts import render
from jobscraper.forms import JobScraperForm
from . import job_scraper as scrapper_script
import random

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
            
            scraped_keys = []
            scraped_values = []
            scraped_colors = []
            for i in scraped: #for every tuple in scraped
                scraped_keys.append(str(i[0]))
                scraped_values.append(str(i[1]))
                c1 = random.randint(0, 255)
                c2 = random.randint(0, 255)
                c3 = random.randint(0, 255)
                scraped_colors.append(str(c1) + ", " + str(c2) + ", " + str(c3) + ", ") 
            
            #print("scraped: " + str(scraped))
            #print("scraped_keys: " + str(scraped_keys))
            #print("scraped_values: " + str(scraped_values))
            #print("scraped_colors: " + str(scraped_colors))

                    
            return render(
                request, 
                'job_scraper/job_scraper.html', 
                {"form": form,
                 "scraped_keys": scraped_keys,
                 "scraped_values": scraped_values,
                 "scraped_colors": scraped_colors,
                 }
            )
        else:
            return render(
                request, 
                'job_scraper/job_scraper.html', 
                {"form": form}
        )
    



