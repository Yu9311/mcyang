from django.http import HttpResponse

from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializer import CourseSerializer, TeacherSerializer, StudentSerializer, SignSerializer, \
    Race_AnswerSerializer, Race_ListSerializer, Sign_RecordSerializer, Team_DescSerializer, TeamSerializer, \
    Team_MemberSerializer, Course_RecordSerializer, QA_TopicSerializer, QuestionSerializer, Answer_MemberSerializer
from .models import Course,Course_Record, Teacher, Student, Sign, Race_Answer, Race_List, Sign_Record, Team_Desc, \
    Team, Team_Member, QA_Topic, Question, Answer_Member


# bg1.老師登入
@csrf_exempt
def login(request):
    return render(request, 'login.html', {})

def user_login(request):
    if request.method =='POST':
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            if Teacher.objects.filter(T_Email=email, T_Password=password).exists():
                return render(request, 'index.html',{})
            else:
                print("Email OR Password Error! Please try again!!!!")
                return redirect('/')
        except Exception as identifier:
            print("Exception!!!!")
            return redirect('/')
    else:
        print("Method IS NOT POST!!!!")
        return render(request, 'login.html', {})

# 1.StudentLoginAPI 學生登入
class StudentLoginViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    lookup_field = 'S_Email'

    def get(self, request, S_Email):
        if S_Email:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

# 2.TeacherLoginAPI 老師登入
class TeacherLoginViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    lookup_field = 'T_Email'

    def get(self, request, T_Email):
        if T_Email:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)


# 3.CourseAPI 老師課程查詢&創建課程
class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    lookup_field = 'T_id'

    # 1
    def get_queryset(self):
        if 'T_id' in self.kwargs:
            return Course.objects.filter(T_id=self.kwargs['T_id'])
        else:
            return Course.objects.all()

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(data=serializer.data)

    def post(self, request):
        return self.create(request)


# 4.Sign 老師開始點名&學生簽到
class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    lookup_field = 'S_id'

    def get(self, request, S_id):
        if S_id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)


class CourseRecordViewSet(ModelViewSet):
    serializer_class = Course_RecordSerializer
    queryset = Course_Record.objects.all()

    lookup_field = 'CR_id'

    def get(self, request, CR_id):
        if CR_id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

class SignViewSet(ModelViewSet):
    serializer_class = SignSerializer
    queryset = Sign.objects.all()

    lookup_field = 'Sign_id'

    def get(self, request, Sign_id):
            return self.list(request)


class SignRecordViewSet(ModelViewSet):
    serializer_class = Sign_RecordSerializer
    queryset = Sign_Record.objects.all()

    lookup_field = 'Sign_id'

    def get_queryset(self):
        if 'Sign_id' in self.kwargs:
            return Sign_Record.objects.filter(Sign_id=self.kwargs['Sign_id'])
        else:
            return Sign_Record.objects.all()

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(data=serializer.data)

    def post(self, request):
        return self.create(request)


# 5.Race_Answer 老師開放搶答&學生開始搶答
class Race_AnswerViewSet(ModelViewSet):
    serializer_class =Race_AnswerSerializer
    queryset = Race_Answer.objects.all()

    lookup_field = 'R_id'

    def get(self, request, R_id):
        if R_id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def update(self, request, R_id):
        stu = Race_Answer.objects.get(R_id=R_id)
        serializer = Race_AnswerSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.retrieve(request)

    def post(self, request):
        return self.create(request)


class Race_ListViewSet(ModelViewSet):
    serializer_class = Race_ListSerializer
    queryset = Race_List.objects.all()

    lookup_field = 'id'

    def get_queryset(self):
        if 'id' in self.kwargs:
            return Race_List.objects.filter(id=self.kwargs['id'])
        else:
            return Race_List.objects.all()

    def update(self, request, id):
        stu = Race_List.objects.get(id=id)
        serializer = Race_ListSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.retrieve(request)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(data=serializer.data)

    def post(self, request):
        return self.create(request)

class Race_List_R_ViewSet(ModelViewSet):
    serializer_class = Race_ListSerializer
    queryset = Race_List.objects.all()

    lookup_field = 'R_id'

    def get_queryset(self):
        if 'R_id' in self.kwargs:
            return Race_List.objects.filter(R_id=self.kwargs['R_id'])
        else:
            return Race_List.objects.all()

    def update(self, request, R_id):
        stu = Race_List.objects.get(R_id=R_id)
        serializer = Race_ListSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.retrieve(request)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(data=serializer.data)

    def post(self, request):
        return self.create(request)


# 6.Team_老師發放隊長跟組員組隊訊號
class Team_DescViewSet(ModelViewSet):
    serializer_class = Team_DescSerializer
    queryset = Team_Desc.objects.all()

    lookup_field = 'C_id'

    def get_queryset(self):
        if 'C_id' in self.kwargs:
            return Team_Desc.objects.filter(C_id=self.kwargs['C_id'])
        else:
            return Team_Desc.objects.all()

    def update(self, request, C_id):
        stu = Team_Desc.objects.get(C_id=C_id)
        serializer = Team_DescSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.retrieve(request)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)

    def post(self, request):
        return self.create(request)

# 組員新增
class TeamLeaderViewSet(ModelViewSet):
    serializer_class = Team_DescSerializer
    queryset = Team.objects.all()

    lookup_field = 'Group_limit'
    


class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    lookup_field = 'Team_id'

    def get_queryset(self):
        if 'Team_id' in self.kwargs:
            return Team.objects.filter(Team_id=self.kwargs['Team_id'])
        else:
            return Team.objects.all()

    def update(self, request, Team_id):
        stu = Team.objects.get(Team_id=Team_id)
        serializer = TeamSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.retrieve(request)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)

    def post(self, request):
        return self.create(request)


class Team_MemberViewSet(ModelViewSet):
    serializer_class = Team_MemberSerializer
    queryset = Team_Member.objects.all()

    lookup_field = 'TeamMember_id'

    def get_queryset(self):
        if 'TeamMember_id' in self.kwargs:
            return Team_Member.objects.filter(TeamMember_id=self.kwargs['TeamMember_id'])
        else:
            return Team_Member.objects.all()

    def update(self, request, TeamMember_id):
        stu = Team_Member.objects.get(TeamMember_id=TeamMember_id)
        serializer = Team_MemberSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.retrieve(request)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)

    def post(self, request):
        return self.create(request)


# 7.QA_老師開始提問跟學生答題
class QA_TopicViewSet(ModelViewSet):
    serializer_class = QA_TopicSerializer
    queryset = QA_Topic.objects.all()

    lookup_field = 'C_id'

    def get_queryset(self):
        if 'C_id' in self.kwargs:
            return QA_Topic.objects.filter(C_id=self.kwargs['C_id'])
        else:
            return QA_Topic.objects.all()

    def update(self, request, C_id):
        stu = QA_Topic.objects.get(C_id=C_id)
        serializer = QA_TopicSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.retrieve(request)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)

    def post(self, request):
        return self.create(request)

class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    lookup_field = 'QA_id'

    def get_queryset(self):
        if 'QA_id' in self.kwargs:
            return Question.objects.filter(QA_id=self.kwargs['QA_id'])
        else:
            return Question.objects.all()

    def update(self, request, QA_id):
        stu = Question.objects.get(QA_id=QA_id)
        serializer = QuestionSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.retrieve(request)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)

    def post(self, request):
        return self.create(request)

class Question_QViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    lookup_field = 'Q_id'

    def get_queryset(self):
        if 'Q_id' in self.kwargs:
            return Question.objects.filter(Q_id=self.kwargs['Q_id'])
        else:
            return Question.objects.all()

    def update(self, request, Q_id):
        stu = Question.objects.get(Q_id=Q_id)
        serializer = QuestionSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.retrieve(request)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)

    def post(self, request):
        return self.create(request)

class Answer_MemberViewSet(ModelViewSet):
    serializer_class = Answer_MemberSerializer
    queryset = Answer_Member.objects.all()

    lookup_field = 'Answer_id'

    def get_queryset(self):
        if 'Answer_id' in self.kwargs:
            return Answer_Member.objects.filter(Answer_id=self.kwargs['Answer_id'])
        else:
            return Answer_Member.objects.all()

    def update(self, request, Answer_id):
        stu = Answer_Member.objects.get(Answer_id=Answer_id)
        serializer = Answer_MemberSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.retrieve(request)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)

    def post(self, request):
        return self.create(request)


