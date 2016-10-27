from django.shortcuts import render
# Create your views here.


def courses(request, template='courses.html'):
    courses = {
        'data': [['Course 1', 'See Course 1 Videos'],
                 ['Course 2', 'See Course 2 Videos'],
                 ['Course 3', 'See Course 3 Videos'],
                 ['Course 4', 'See Course 4 Videos']],
        'videos': ['this is a video 1', 'this is a video 2',
                   'this is a video 3', 'this is a video 4',
                   'this is a video 5', 'this is a video 6',
                   'this is a video 7', 'this is a video 8',
                   'this is a video 9', 'this is a video 10',
                   'this is a video 11', 'this is a video 12',
                   'this is a video 13', 'this is a video 14',
                   'this is a video 15', 'this is a video 16',
                   'this is a video 17', 'this is a video 18',
                   'this is a video 19', 'this is a video 20'],
    }
    return render(request, template, courses)
