from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tags,Questions
import json
from django.core import serializers
# Create your views here.
@csrf_exempt
def CreateTag(request):
    if(request.method=="POST"):
        try:
            request_data = request.body
            decode_request_data = request.body.decode('utf-8')
            requestDataJson = json.loads(decode_request_data)
            tags=Tags.objects.filter(Name=requestDataJson['Tag'])
            if(len(tags)==0):
                tag=Tags.objects.create(Name=requestDataJson['Tag'])
                tag.save()
                messageData={
                    "responseType":"success",
                    "messageType":"success",
                    "message":"Tag Created Successfully",
                    "responseData":tag.Name
                }
                return(JsonResponse(messageData,status=200))
            messageData={
                "responseType":"success",
                "messageType":"error",
                "message":"Tag Already Exists",
                "responseData":tags[0].Name
            }
            return(JsonResponse(messageData,status=200))
        except:
            messageData={
                "responseType":"success",
                "messageType":"error",
                "message":"Inconsistent Data Provided",
                "responseData":''
            }
            return(JsonResponse(messageData,status=200))


    if(request.method=="GET"):
        return(render(request,"CreatingTags.html"))
        pass

@csrf_exempt
def CreateQuestions(request):
    if(request.method=="POST"):
        try:
            request_data=request.body
            decode_request_data = request.body.decode('utf-8')
            requestDataJson = json.loads(decode_request_data)
            return(HttpResponse(requestDataJson['Text']))
            title,difficulty,acceptance,submissions=requestDataJson['Title'],requestDataJson['Difficulty'],requestDataJson['Acceptance'],requestDataJson['Submissions']
            likes,dislikes,text,tags=requestDataJson['Likes'],requestDataJson['DisLikes'],requestDataJson['Text'],requestDataJson['Tags']
            question=Questions(Title=title)
            question.Difficulty,question.Acceptance,question.Submissions=difficulty,acceptance,submissions
            question.Likes,question.DisLikes,question.Text=likes,dislikes,text
            question.save()
            for i in tags:
                tag=Tags.objects.get(Name=i)
                question.Tags.add(tag)
            question.save()
            messageData={
                    "responseType":"success",
                    "messageType":"success",
                    "message":"Question Created Successfully",
                    "responseData":question.id
                }
            return(JsonResponse(messageData,status=200))
        except:
            messageData={
                "responseType":"success",
                "messageType":"error",
                "message":"Inconsistent Data Provided",
                "responseData":''
            }
            return(JsonResponse(messageData,status=200))
    else:
        #Render UI
        pass



def Problems(request):
    if(request.method=="GET"):
        questions=Questions.objects.all()
        questions=serializers.serialize('json',questions)
        messageData={
                    "responseType":"success",
                    "messageType":"success",
                    "message":"Question Fetched Succesfully",
                    "responseData":questions
                }
        return(JsonResponse(messageData,status=200))

def TagProblems(request,TAG):
    if(request.method=="GET"):
        TAG=TAG.replace("-"," ")
        questions=Questions.objects.filter(Tags__Name=TAG)
        questions=serializers.serialize('json',questions)
        messageData={
                    "responseType":"success",
                    "messageType":"success",
                    "message":"Question Fetched Succesfully",
                    "responseData":questions
                }
        return(JsonResponse(messageData,status=200))
