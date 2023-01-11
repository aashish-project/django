from django.shortcuts import render,HttpResponse ,redirect,get_object_or_404
from .models import*
# Create your views here.
from django.http import HttpResponseNotFound

def favicon(request):
    return HttpResponseNotFound()

def home(request,branch_slug=None,subject_slug=None,chapter_slug=None,topic_slug=None):
    if(branch_slug=='favicon.ico'):
        return HttpResponse("Something went wrong")
    # Retrieve the Branch, Subject, and Chapter objects based on the slugs
    data=[]
    branches=Branch.objects.all()
    for branch in branches:
        data.append({
            "branch":branch,
            "subjects":list(branch.subject_set.all()),
            "chapter":[]
        })
    if subject_slug!=None and data[0]['branch']!=branch_slug:
        # print(query)
        branch=Branch.objects.get(branch=branch_slug)
            # print(branch)
        sub=branch.subject_set.get(subject=subject_slug)
        data.append({"subject_select":sub})
        for chapter in sub.chapter_set.all():
            chapter = str(chapter).split(':')
            data[2]['chapter'].append(chapter)
                    
    if chapter_slug!=None:
        # print(request.GET.get('chapter'))
        topics=[]
        chapter=Chapter.objects.get(chapter=chapter_slug)
        topic=chapter.topic_set.all()
        for item in topic:
            topics.append(str(item)) 
        print(topics)
        data.append({"topics":topics})
    if topic_slug!=None:
        data.append({
            "topic_select":topic_slug
        })
        # topic(request,data,branch_slug,subject_slug,chapter_slug,topic_slug)
    if "topic_select" in data[0]:
        print(data[0]['topic_select'])
    print(f"\n {branch_slug,subject_slug,chapter_slug}")
    print(branch_slug)
    return render(request,"home.html",{'branch_data':data})


# def topic(request,data,branch_slug=None,subject_slug=None,chapter_slug=None,topic_slug=None):
#     chapters=Chapter.objects.all()
#     for chapter in chapters:
#         if(str(chapter)==chapter_slug):
#             print(chapter_slug)
#             data.append({
#                 "topic":list(chapter.topic_set.all()),
#             })
#     if topic_slug!=None:
#         print(topic_slug)
#     # print(data_topic)
#     return render(request,"topic.html",{"branch_data":data})


def temp(request):
    return render(request,"temp.html")