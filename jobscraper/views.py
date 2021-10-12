from django.shortcuts import render

# Create your views here.
def job_scraper(request):
    return render(request, 'job_scraper/job_scraper.html')