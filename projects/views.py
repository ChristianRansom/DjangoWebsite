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
    0:  {
            'name': 'productiveprogrammer.me ',
            'description': 'A personal portfolio and blog',
            'explanation': 'A personal portfolio and blog to show off my projects and interests. Currently a work in progress. ',
            'date': 'October 2021 - Present',
            'link': 'link',
            'image': 'img/project1.png',
            'skills': 'skills',
        },
    1:  {
            'name': 'DjangoWebBoards ',
            'description': 'A simple forum website',
            'explanation': 'A Forum and Topic System built with Django created from following this excellent tutorial https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/',
            'date': 'Sep 2019 - Aug 2019',
            'link': 'link',
            'image': 'img/project1.png',
            'skills': 'skills',
        },
    2:  {
            'name': 'DeepNeuralNetworks ',
            'description': 'Learning Machine Learning',
            'explanation': 'An implementation from scratch of deep neural networks. Allows for the creation of multilayered networks that train through supervised learning and backpropagation.',
            'date': 'Feb 2019 - March 2019',
            'link': 'link',
            'image': 'img/project2.png',
            'skills': 'skills',
        },
    3:  {
            'name': 'CommandSchedulerPlus ',
            'description': 'A Minecraft plugin that schedules commands',
            'explanation': 'A lightweight plugin that schedules commands across restarts and long periods. This project uses a complex data structure (AVL Tree) to handle the data.',
            'date': 'Oct 2017 - Feb 2018',
            'link': 'link',
            'image': 'img/project3.png',
            'skills': 'skills',
        },
    4:  {
            'name': 'DodgerBall',
            'description': 'A simple android game',
            'explanation': 'A simple Android game written in Java. This project taught me about the Android Development Environment.',
            'date': 'Jan 2016 - Jun 2016',
            'link': 'link',
            'image': 'img/project3.png',
            'skills': 'skills',
        },
    5:  {
            'name': 'Snake',
            'description': 'Python Game',
            'explanation': 'A game written in Python using Pygame and TkInter. I was the technical lead on this project and led three other developers to make contributions to the project. ',
            'date': 'Feb 2019 - Jun 2019',
            'link': 'link',
            'image': 'img/project3.png',
            'skills': 'skills',
        },
    }
