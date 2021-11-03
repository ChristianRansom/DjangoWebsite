import random
import string
from resume.resume_data import *

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
