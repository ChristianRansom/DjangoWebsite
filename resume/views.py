from resume.resume_data import *
import os
from django.conf import settings
from django.http import HttpResponse, Http404

from django.shortcuts import render


def resume_index(request):
    context = {
        'projects': projects,
        'experience': experience,
        'skills': skills,
        'skill_list': skill_list,
    }
    return render(request, 'resume_index.html', context)


def project_detail(request, pk):
    context = {
        'project': projects[pk]
    }
    return render(request, 'project_detail.html', context)


def download(request, path):
    file_path = os.path.join(settings.STATIC_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404