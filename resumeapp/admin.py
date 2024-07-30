from django.contrib import admin
from resumeapp.models import CodingLanguage, CodingTool, IndividualAssignment, IndividualProject, GroupProject

# Models





admin.site.register(CodingLanguage)
admin.site.register(CodingTool)
admin.site.register(IndividualAssignment)
admin.site.register(IndividualProject)
admin.site.register(GroupProject)