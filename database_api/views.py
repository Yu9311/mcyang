from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from .serializer import LoginSerializer, CourseSerializer, TeacherSerializer, StudentSerializer, SignSerializer, \
    Race_AnswerSerializer, Race_ListSerializer, Sign_RecordSerializer, Team_DescSerializer, TeamSerializer, \
    Team_MemberSerializer
from .models import Course, Teacher, Student, Sign, Race_Answer, Race_List, Sign_Record, Team_Desc, Team, Team_Member


# LoginAPI
class StudentLoginApiView(APIView):
    def post(self, request):
        self.as_view()
        check = False
        data = json.loads(request.body)
        S_Email = data['S_Email']
        for i in Student.objects.get("S_Email"):
            if S_Email is i:
                check = True
            else:
                check = False

        if check:
            return Response(S_Email)
        else:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)


class StudentLoginDetail(APIView):
    # 2
    def get_object(self, S_Email):
        self.as_view()
        try:
            email = S_Email.query_params['email']
            password = S_Email.query_params['password']
            return Student.objects.get(S_Email=S_Email)
        except Student.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # 4
    def get(self, request, S_Email):
        email = self.get_object(S_Email)
        serializer = LoginSerializer(email)
        return Response(serializer.data)


# CourseAPI
class CourseApiView(APIView):
    # 1
    def get(self, request):
        self.as_view()
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    # 2
    def post(self, request):
        self.as_view()
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    # 3
    def get_object(self, C_id):
        self.as_view()
        try:
            return Course.objects.get(C_id=C_id)
        except Course.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # 4
    def get(self, request, C_id):
        course = self.get_object(C_id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


# Student API
class StudentApiView(APIView):
    # 1
    def get(self, request):
        self.as_view()
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    # 2
    def post(self, request):
        self.as_view()
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    # 3
    def get_object(self, S_id):
        self.as_view()
        try:
            return Student.objects.get(S_id=S_id)
        except Student.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # 4
    def get(self, request, S_id):
        student = self.get_object(S_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)


# Teacher
class TeacherApiView(APIView):
    # 1
    def get(self, request):
        self.as_view()
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)

    # 2
    def post(self, request):
        self.as_view()
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetail(APIView):
    # 3
    def get_object(self, T_id):
        self.as_view()
        try:
            return Teacher.objects.get(T_id=T_id)
        except Teacher.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # 4
    def get(self, request, T_id):
        teacher = self.get_object(T_id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)


# Sign
class SignApiView(APIView):
    # 1
    def get(self, request):
        self.as_view()
        sign = Sign.objects.order_by('Sign_id')
        serializer = SignSerializer(sign, many=True)
        return Response(serializer.data)

    # 2
    def post(self, request):
        self.as_view()
        serializer = SignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignDetail(APIView):
    # 3
    def get_object(self, Sign_id):
        self.as_view()
        try:
            return Sign.objects.get(Sign_id=Sign_id)
        except Sign.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # 4
    def get(self, request, Sign_id):
        Sign = self.get_object(Sign_id)
        serializer = SignSerializer(Sign)
        return Response(serializer.data)


# Race_Answer
class Race_AnswerApiView(APIView):
    # 1
    def get(self, request):
        self.as_view()
        race_answer = Race_Answer.objects.order_by('R_id')
        serializer = SignSerializer(race_answer, many=True)
        return Response(serializer.data)

    # 2
    def post(self, request):
        self.as_view()
        serializer = Race_AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Race_AnswerDetail(APIView):
    # 3
    def get_object(self, R_id):
        self.as_view()
        try:
            return Sign.objects.get(R_id=R_id)
        except Sign.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # 4
    def get(self, request, R_id):
        race_answer = self.get_object(R_id)
        serializer = Race_AnswerSerializer(race_answer)
        return Response(serializer.data)


# Race_List
class Race_ListApiView(APIView):
    # 1
    def get(self, request):
        self.as_view()
        race_list = Race_List.objects.order_by('Time')
        serializer = Race_ListSerializer(race_list, many=True)
        return Response(serializer.data)

    # 2
    def post(self, request):
        self.as_view()
        serializer = Race_ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Race_ListDetail(APIView):
    # 3
    def get_object(self, R_id):
        self.as_view()
        try:
            return Sign.objects.get(R_id=R_id)
        except Sign.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # 4
    def get(self, request, Sign_id):
        Sign = self.get_object(Sign_id)
        serializer = SignSerializer(Sign)
        return Response(serializer.data)


# Sign_Record
class Sign_RecordApiView(APIView):
    # 1
    def get(self, request):
        self.as_view()
        sign_record = Sign_Record.objects.order_by('SR_id')
        serializer = Sign_RecordSerializer(sign_record, many=True)
        return Response(serializer.data)

    # 2
    def post(self, request):
        self.as_view()
        serializer = Sign_RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Sign_RecordDetail(APIView):
    # 3
    def get_object(self, SR_id):
        self.as_view()
        try:
            return Sign.objects.get(SR_id=SR_id)
        except Sign.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # 4
    def get(self, request, SR_id):
        Sign_Record = self.get_object(SR_id)
        serializer = Sign_RecordSerializer(Sign_Record)
        return Response(serializer.data)


# Team_Desc
class Team_DescApiView(APIView):
    # 1
    def get(self, request):
        self.as_view()
        team_desc = Team_Desc.objects.order_by('TeamDesc_id')
        serializer = Sign_RecordSerializer(team_desc, many=True)
        return Response(serializer.data)

    # 2
    def post(self, request):
        self.as_view()
        serializer = Team_DescSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Team_DescDetail(APIView):
    # 3
    def get_object(self, TeamDesc_id):
        self.as_view()
        try:
            return Sign.objects.get(TeamDesc_id=TeamDesc_id)
        except Sign.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # 4
    def get(self, request, TeamDesc_id):
        Team_Desc = self.get_object(TeamDesc_id)
        serializer = Team_DescSerializer(Team_Desc)
        return Response(serializer.data)


# Team
class TeamApiView(APIView):
    # 1
    def get(self, request):
        self.as_view()
        team = Team.objects.order_by('Team_id')
        serializer = Sign_RecordSerializer(team, many=True)
        return Response(serializer.data)

    # 2
    def post(self, request):
        self.as_view()
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetail(APIView):
    # 3
    def get_object(self, Team_id):
        self.as_view()
        try:
            return Sign.objects.get(Team_id=Team_id)
        except Sign.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # 4
    def get(self, request, Team_id):
        Team = self.get_object(Team_id)
        serializer = TeamSerializer(Team)
        return Response(serializer.data)


# Team_Member
class Team_MemberApiView(APIView):
    # 1
    def get(self, request):
        self.as_view()
        team_member = Team.objects.order_by('TeamMember_id')
        serializer = Sign_RecordSerializer(team_member, many=True)
        return Response(serializer.data)

    # 2
    def post(self, request):
        self.as_view()
        serializer = Team_MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Team_MemberDetail(APIView):
    # 3
    def get_object(self, TeamMember_id):
        self.as_view()
        try:
            return Sign.objects.get(TeamMember_id=TeamMember_id)
        except Team_Member.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # 4
    def get(self, request, TeamMember_id):
        Team_Member = self.get_object(TeamMember_id)
        serializer = TeamSerializer(Team_Member)
        return Response(serializer.data)
