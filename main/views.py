'''Main View'''
from collections import OrderedDict
from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb
import os

# Create your views here.
DATABASES = {
    'NAME': 'tutorial',
    'USER': 'root',
    'PASSWORD': 'pass',
    'HOST': 'localhost',
}

conn = MySQLdb.connect(host=DATABASES['HOST'], user=DATABASES['USER'],
                       passwd=DATABASES['PASSWORD'], db=DATABASES['NAME'])


def home(request, template='index.html'):
    '''Home Function'''
    cursor = conn.cursor()

    videoData = OrderedDict()
    query = 'SELECT DISTINCT(course_name) FROM video_data'

    cursor.execute(query)
    results = cursor.fetchall()

    for result in results:
        videoData[result[0]] = []

    query = 'SELECT course_name, video_title, video_link FROM video_data \
    ORDER BY course_name, video_title'

    cursor.execute(query)
    results = cursor.fetchall()

    for result in results:
        videoData[result[0]].append([result[1].strip().split(' | ')[1].strip(), result[2].strip()])

    courses = {
        'videoData': []
        }
    for key in videoData:
        courses['videoData'].append([key, videoData[key]])

    return render(request, template, courses)


def contact(request):
    '''Contact Function'''
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        if name and email and message:
            query = 'INSERT INTO contact_data SET name = "%s", email = "%s",\
            subject = "%s", message = "%s"'
            cursor.execute(query % (name, email, subject, message))

        cursor.close()
        conn.commit()

    return HttpResponse('')

def courses(request, template='courses.html'):
    '''Courses Function'''
    cursor = conn.cursor()

    videoData = OrderedDict()
    query = 'SELECT DISTINCT(course_name) FROM video_data'

    cursor.execute(query)
    results = cursor.fetchall()

    for result in results:
        videoData[result[0]] = []

    query = 'SELECT course_name, video_title, video_link FROM video_data \
    ORDER BY course_name, video_title'

    cursor.execute(query)
    results = cursor.fetchall()

    for result in results:
        videoData[result[0]].append([result[1].strip(), result[2].strip()])

    courses = {
        'videoData': [],
        }
    for key in videoData:
        courses['videoData'].append([key, videoData[key]])

    return render(request, template, courses)
