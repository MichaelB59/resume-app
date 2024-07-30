from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# idea: include screenshots, or images

class CodingLanguage(models.Model):
    lang_name = models.CharField(max_length=50)
    lang_timespent = models.FloatField() # want/need? units?
    lang_proj_worked = models.IntegerField() # number of projects that have used this projects, that I have been on

    def __str__(self):
        return self.lang_name

class CodingTool(models.Model):
    tool_name = models.CharField(max_length=50)
    tool_timespent = models.FloatField() # want/need? units?
    tool_project_worked = models.IntegerField() # number of projects that have used this projects, that I have been on

    def __str__(self):
        return self.tool_name

class IndividualProject(models.Model):
    iproj_name = models.CharField(max_length=50)
    iproj_desc = models.CharField(max_length=300)
    iproj_lang_utilized = models.CharField(max_length=300) # relationship to coding languages
    iproj_tools_used = models.CharField(max_length=300) # char or array field? Purpose: List of IDE's & etc used in the making and publishing, etc of the project
    iproj_timespent = models.FloatField() # want/need? units?
    iproj_github_link = models.URLField() # link to the project on github

    def __str__(self):
        return self.iproj_name

class IndividualAssignment(models.Model):
    iassign_name = models.CharField(max_length=50)
    iassign_desc = models.CharField(max_length=300)
    iassign_lang_utilized = models.CharField(max_length=300) # relationship to coding languages
    iassign_tools_used = models.CharField(max_length=300) # char or array field? Purpose: List of IDE's & etc used in the making and publishing, etc of the project
    iassign_timespent = models.FloatField() # want/need? units?
    iassign_github_link = models.URLField() # link to the project on github

    def __str__(self):
        return self.iassign_name

class GroupProject(models.Model):
    gproj_name = models.CharField(max_length=50)
    gproj_desc = models.CharField(max_length=300)
    gproj_lang_utilized = models.CharField(max_length=300) # relationship to coding languages
    gproj_tools_used = models.CharField(max_length=300) # char or array field? Purpose: List of IDE's & etc used in the making and publishing, etc of the project
    gproj_timespent = models.FloatField() # want/need? units?
    gproj_github_link = models.URLField() # link to the project on github

    def __str__(self):
        return self.gproj_name