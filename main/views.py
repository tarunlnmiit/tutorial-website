from django.shortcuts import render

# Create your views here.


def home(request, template='index.html'):
    courses = {
        'data': [['Course 1', 'See Course 1 Videos'],
                 ['Course 2', 'See Course 2 Videos'],
                 ['Course 3', 'See Course 3 Videos'],
                 ['Course 4', 'See Course 4 Videos']],
        'videos': ['vid 1', 'vid 2', 'vid 3', 'vid 4', 'vid 5'],
    }
    return render(request, template, courses)
