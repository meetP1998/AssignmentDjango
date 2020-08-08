from django.shortcuts import render
from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import *
from .models import *
from django.contrib.auth.models import User
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions, pagination
from rest_framework import serializers
import json
# Create your views here.

class Result(APIView):
    def get(self,request,*args,**kwargs):
        res_dict={}
        user_data=User_Data.objects.all()
        final_list=[]
        if user_data.count()>0:
            for obj1 in user_data:
                r1={}
                r1["id"]=obj1.uid
                r1["real_name"]=obj1.real_name
                r1["tz"]=obj1.tz
                acti_objs=Activity_Mapping.objects.filter(user_activity_id=obj1)
                list=[]
                if acti_objs.count()>0:
                    print(acti_objs.count())
                    for obj2 in acti_objs:
                        r2={}
                        r2["start_time"]=obj2.start_time
                        r2["end_time"]=obj2.end_time
                        list.append(r2)
                r1["activity_periods"]=list
                final_list.append(r1)
            res_dict["ok"]=True
            res_dict["members"]=final_list
            return Response(res_dict,status.HTTP_200_OK)
        res_dict["ok"]=False
        return Response(res_dict,status.HTTP_404_NOT_FOUND)
