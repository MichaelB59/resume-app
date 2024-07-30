from resumeapp.models import CodingLanguage, CodingTool, IndividualAssignment, IndividualProject, GroupProject
from resumeapp.api.serializer import CodingLanguageSerializer, CodingToolSerializer, IndividualAssignmentSerializer, IndividualProjectSerializer, GroupProjectSerialzer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from django.shortcuts import render
from django.views.generic import TemplateView
import requests


class CodingLanguageList(viewsets.ViewSet):
    def get_view_name(self):
        return "Coding Languages"
    
    def get_view_description(self, html=False):
        return "These are the languages that I have worked with ranging from aware to more familiar."

    def list(self, request):
        queryset = CodingLanguage.objects.all()
        serializer = CodingLanguageSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = CodingLanguage.objects.all()
        cl = get_object_or_404(queryset, pk=pk)
        serializer = CodingLanguageSerializer(cl)
        return Response(serializer.data)

class CodingLanguageListView(TemplateView):
    template_name = "coding_language_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get('http://127.0.0.1:8000/api/resume/cl/')
        context['languages'] = response.json()
        return context

class CodingToolList(viewsets.ViewSet):
    def get_view_name(self):
        return "Coding Tools"
    
    def get_view_description(self, html=False):
        return "These are the tools & IDE's that I have worked with ranging from aware to more familiar."
    
    def list(self, request):
        queryset = CodingTool.objects.all()
        serializer = CodingToolSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = CodingTool.objects.all()
        ct = get_object_or_404(queryset, pk=pk)
        serializer = CodingToolSerializer(ct)
        return Response(serializer.data)

class IndividualAssignmentList(viewsets.ViewSet):
    def get_view_name(self):
        return "Individual Class Assignments"
    
    def get_view_description(self, html=False):
        return "These are the individual class assignments I have completed."
    
    def list(self, request):
        queryset = IndividualAssignment.objects.all()
        serializer = IndividualAssignmentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = IndividualAssignment.objects.all()
        ia = get_object_or_404(queryset, pk=pk)
        serializer = IndividualAssignmentSerializer(ia)
        return Response(serializer.data) 

class IndividualProjectList(viewsets.ViewSet):
    template_name = "coding_language_list.html"

    def get_view_name(self):
        return "Individual Projects"
    
    def get_view_description(self, html=False):
        return "These are the individual projects I have completed."

    def list(self, request):
        queryset = IndividualProject.objects.all()
        serializer = IndividualProjectSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = IndividualProject.objects.all()
        ip = get_object_or_404(queryset, pk=pk)
        serializer = IndividualProjectSerializer(ip)
        return Response(serializer.data)

class GroupProjectList(viewsets.ViewSet):
    def get_view_name(self):
        return "Individual Assignments"
    
    def get_view_description(self, html=False):
        return "These are the individual assignments I have completed, all of these projects I worked on with a group of 3 or more."

    def list(self, request):
        queryset = GroupProject.objects.all()
        serializer = GroupProjectSerialzer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = GroupProject.objects.all()
        gp = get_object_or_404(queryset, pk=pk)
        serializer = GroupProjectSerialzer(gp)
        return Response(serializer.data)             