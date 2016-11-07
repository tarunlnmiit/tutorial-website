from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb

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
    cursor = conn.cursor()

    courses = {
        'data': [['Course 1', 'See Course 1 Videos', [
            'vid 1', 'vid 2', 'vid 3', 'vid 4', 'vid 5']],
            ['Course 2', 'See Course 2 Videos', [
                'vid 1', 'vid 2', 'vid 3', 'vid 4', 'vid 5']],
            ['Course 3', 'See Course 3 Videos', [
                'vid 1', 'vid 2', 'vid 3', 'vid 4', 'vid 5']],
            ['Course 4', 'See Course 4 Videos', [
                'vid 1', 'vid 2', 'vid 3', 'vid 4', 'vid 5']]],
        'videos': ['vid 1', 'vid 2', 'vid 3', 'vid 4', 'vid 5'],
    }
    return render(request, template, courses)


def contact(request):
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
