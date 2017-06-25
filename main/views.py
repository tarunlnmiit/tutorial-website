'''Main View'''
import os
from collections import OrderedDict
from django.shortcuts import render
from .models import Videos

# Create your views here.


def home(request, template='index.html'):
    '''Home Function'''
    videoData = dict()

    coursesList = Videos.objects.values_list('course_name').distinct()
    for course in coursesList:
        videoData[course[0]] = []

    videosDataList = Videos.objects.values_list('course_name', 'video_title', 'video_link').order_by('course_name', 'video_title')

    for result in videosDataList:
        videoData[result[0]].append([result[1].strip().split(' | ')[1].strip(), result[2].strip()])

    courses = {
        'videoData': []
        }
    videoData = dict.fromkeys(sorted(videoData.keys()))
    for key in videoData:
        courses['videoData'].append([key, videoData[key]])

    return render(request, template, courses)

