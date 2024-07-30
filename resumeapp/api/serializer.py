from rest_framework import serializers
from resumeapp.models import CodingLanguage, CodingTool, IndividualAssignment, IndividualProject, GroupProject

class CodingLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CodingLanguage
        fields = "__all__"

class CodingToolSerializer(serializers.ModelSerializer)        :

    class Meta:
        model = CodingTool
        fields = "__all__"

class IndividualAssignmentSerializer(serializers.ModelSerializer)        :

    class Meta:
        model = IndividualAssignment
        fields = "__all__"

class IndividualProjectSerializer(serializers.ModelSerializer)        :

    class Meta:
        model = IndividualProject
        fields = "__all__"

class GroupProjectSerialzer(serializers.ModelSerializer):

    class Meta:
        model = GroupProject
        fields = "__all__"