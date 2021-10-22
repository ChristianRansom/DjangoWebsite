from django.shortcuts import render
from projects.models import Project








def project_index(request):

    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)



def project_detail(request, pk):
    context = {
        'project': projects[pk]
    }
    return render(request, 'project_detail.html', context)



projects = {
    1:  {
            'name': 'name',
            'description': 'description',
            'explanation': 'explanation',
            'date': 'date',
            'link': 'link',
            'image': 'project1',
            'skills': 'skills',
        },
    2:  {
            'name': 'name',
            'description': 'description',
            'explanation': 'explanation',
            'date': 'date',
            'link': 'link',
            'image': 'project2',
            'skills': 'skills',
        },
    3:  {
            'name': 'name',
            'description': 'description',
            'explanation': 'explanation',
            'date': 'date',
            'link': 'link',
            'image': 'project3',
            'skills': 'skills',
        },
    }
