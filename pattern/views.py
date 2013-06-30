from django.shortcuts import render_to_response
from pattern.models import *
from django.http import HttpResponse

import json

def index(request):
    return render_to_response('index.html')
   
def raw(request):
    return render_to_response("raw.html")
   
def to_json(plist):
    ps = []
    for p in plist:
        a = {}
        a['name'] = p.name
        a['tags'] = [{'name':t.name, 'icon':t.icon} for t in p.tags.all()]
        a['description'] = p.description
        a['intent'] = p.intent
        a['motivation'] = p.motivation
        a['structure'] = p.structure
        a['consequences'] = p.consequences
        a['implementations'] = []
        for i in p.implementations.all():
            b =  {}
            b['gist'] = i.gist
            b['gist_url'] = "https://gist.github.com/%s.js" % str(i.gist) 
            if i.file is not None and i.file != "":
                b['gist_url'] += "?file="+i.file
            b['id'] = i.id
            b['language'] = i.language.name
            b['language_url'] = i.language.wikipedia
            b['language_super'] = i.language.super_lang == None
            a['implementations'].append(b)
            
        a['uses'] = []
        for i in p.uses.all():
            b =  {}
            b['url'] = i.url
            b['name'] = i.name
            b['line_start'] = i.line_start
            b['line_end'] = i.line_end
            b['languages'] = []
            for lang in i.language.all():
                w = {}
                w['language'] = lang.name
                w['language_url'] = lang.wikipedia
                w['language_super'] = lang.super_lang == None
                b['languages'].append(w)
            a['uses'].append(b)
        
        ps.append(a)
    return ps

def list_patterns(request):
    l = [{'name':ll.name, 'url':'#patterns/'+str(ll.id)} for ll in Pattern.objects.all()]
    return HttpResponse(json.dumps(l), content_type="text/json")

def list_tags(request):
    l = [{'name':ll.name, 'url':'#tags/'+str(ll.id)} for ll in Tags.objects.all()]
    return HttpResponse(json.dumps(l), content_type="text/json")

def list_langs(request):
    l = [{'name':ll.name, 'url':'#langs/'+str(ll.id)} for ll in Language.objects.all()]
    return HttpResponse(json.dumps(l), content_type="text/json")

def get_pattern(request, id):
    return HttpResponse(json.dumps(to_json([Pattern.objects.get(id=id)])), content_type="text/json")

def get_tag(request, id):
    return HttpResponse(json.dumps(to_json(Pattern.objects.filter(tags__id__contains = id))), content_type="text/json")

def get_lang(request, id):
    l = Language.objects.get(id=id)
    return HttpResponse(json.dumps(to_json(Pattern.objects.filter(implementations__language__id = id))), content_type="text/json")
    
def all(request):
    return HttpResponse(json.dumps(to_json(Pattern.objects.all())), content_type="text/json")
 
def random(request):
    return HttpResponse(json.dumps(to_json([Pattern.objects.order_by('?')[0]])), content_type="text/json")
    
  
            
            
            
    