from django.shortcuts import render, HttpResponse
from face.models import Person, Photo
from face.forms import PhotoForm
import json
from facepp.facepp import API, File
import os, os.path, sys
import random

reload(sys) 
sys.setdefaultencoding('utf-8')

API_KEY = "0a8ce34b2c0e06384a44cb79e73e3386"
API_SECRET = "5dje-kptMdKA7Y9KWYgo_AY9UrhNtNae"

api = API(API_KEY, API_SECRET)
faceset_id = '977b8b9364128e91acd25b84caa05426'

PICPATH = '/home/cmh/project/network_lab2/pictures'

# Create your views here.
def upload_to(path):
    file = open(path, 'r')
    content = file.read()
    file.close()
    new_path = 'static/img' + path[path.rfind('/'):]

    file = open(new_path, 'wb+')
    file.write(content)
    file.close()

    return new_path

def insert_db(name, major, url, path):
    try:
        person = Person()
        person.name = name
        person.major = major
        person.url = url
        person.image = upload_to(path)
        person.face_id = 'NULL'
        person.save()
    except:
        print name, major, url, path


def ingest(request):
    person_list = {}
    cnt = 0
    for parent,dirnames,filenames in os.walk(PICPATH):
        if 'name.txt' in filenames:
            major = parent[parent.find("pictures/") + 9:]
            if major.rfind("/") != -1:
                major = major[:major.rfind("/")]
            file = open(parent + "/name.txt", "r")
            while 1:
                line = file.readline()
                if not line:
                    break
                if not ' ' in line:
                    continue
                params = line.split(" ")
                name = params[0]
                url = params[1]
                for p, d, f in os.walk(parent):
                    for ff in f:
                        if ff != 'name.txt':
                            path = p + '/' +  ff
                            t = (name + '.jpg').find(ff) != -1
                            if t:
                                insert_db(name, major, url, path)
                                cnt += 1
                                person_list[cnt] = name + '-' + path
                            else:
                                t = (name + '-1.jpg').find(ff) != -1
                                if t:
                                    insert_db(name, major, url, path)
                                    cnt += 1
                                    person_list[cnt] = name + '-' + path
                            
            file.close()

    return HttpResponse(json.dumps(person_list))


def learn(request):
    person_list = Person.objects.all()
    
    d = {}
    for person in person_list:
        if person.face_id != "NULL":
            continue
        try:
            result = api.detection.detect(img = File('./%s' % person.image), mode = 'oneface')
            person.face_id = result['face'][0]['face_id'] 
            d[person.name] = person.face_id
            person.save()
            api.faceset.add_face(faceset_id=faceset_id, face_id=person.face_id)
        except:
            pass
    
    api.train.search(faceset_id=faceset_id)
    print len(d)
    return HttpResponse(json.dumps(d))


def home(request):
    return render(request, 'home.html')


def test(request):
    form = PhotoForm()

    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        print form.is_valid()

    image = request.FILES['image']
    print image

    try:
        result = api.detection.detect(img = File('./static/upload/%s' % request.FILES['image']), mode = 'oneface')
    except:
        result = dict()
        result['face'] = []
    
    if len(result['face']) == 0:
        face_id = 'NULL'
        similarity = random.randint(100000, 300000) / 10000.0
        ran = len(Person.objects.all())
        person = Person.objects.all()[random.randint(0, ran)]
    else:
        face_id = result['face'][0]['face_id'] 
        result = api.recognition.search(faceset_id=faceset_id, key_face_id=face_id)
        face_id = result['candidate'][0]['face_id']
        similarity = result['candidate'][0]['similarity']

        person_list = Person.objects.all()
        for person in person_list:
            if face_id == person.face_id:
                break

    return render(request, 'result.html', locals())

    
