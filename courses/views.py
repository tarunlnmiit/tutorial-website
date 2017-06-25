from django.http import HttpResponse
from django.shortcuts import render
from main.models import Videos
# Create your views here.


def courses(request, template='courses.html'):
    '''Courses Function'''
    videoData = dict()

    coursesList = Videos.objects.values_list('course_name').distinct()
    for course in coursesList:
        videoData[course[0]] = []

    videosDataList = Videos.objects.values_list('course_name', 'video_title', 'video_link').order_by('course_name', 'video_title')

    for result in videosDataList:
        videoData[result[0]].append([result[1].strip(), result[2].strip()])

    courses = {
        'skillLevels': ['Beginner', 'Intermediate', 'Advanced'],
        'categories': ['All', 'Programming', 'Communication', 'Front-End Design'],
        'technolgies': ['Python', 'HTML', 'CSS'],
        'videoData': [],
    }
    for key in videoData:
        courses['videoData'].append([key, videoData[key]])

    return render(request, template, courses)


def search(request):
    '''Search Function'''
    errors = []
    if 'searchTerm' in request.GET:
        searchTerm = request.GET['searchTerm']
    if not searchTerm:
        errors.append('Enter a search term.')
    elif len(searchTerm) > 20:
        errors.append('Please enter at most 20 characters.')
    else:
        results = Videos.objects.filter(course_name__icontains=searchTerm).distinct()
        return render(request, 'searchResults.html',
                      {'courses': results, 'query': searchTerm})
    return render(request, 'index.html',
                  {'errors': errors})