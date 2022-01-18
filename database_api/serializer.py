from rest_framework import serializers
from .models import Course, Teacher, Student, Sign, Race_Answer, Race_List, Sign_Record, Team_Desc, Team, Team_Member


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['S_Email', 'S_Password']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['S_id', 'S_Name']


class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign
        fields = '__all__'


class Race_AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race_Answer
        fields = '__all__'


class Race_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race_List
        fields = '__all__'


class Sign_RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign_Record
        fields = '__all__'


class Team_DescSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_Desc
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class Team_MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_Member
        fields = '__all__'
