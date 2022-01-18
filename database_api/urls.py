from django.urls import path, re_path
from .views import StudentLoginApiView,CourseApiView, CourseDetail, TeacherApiView, TeacherDetail, StudentApiView, StudentDetail, \
    SignApiView, SignDetail, Race_AnswerApiView, Race_AnswerDetail, Race_ListApiView, Race_ListDetail, Sign_RecordApiView, Sign_RecordDetail, TeamApiView, TeamDetail, Team_DescApiView, Team_DescDetail, Team_MemberApiView, Team_MemberDetail

urlpatterns = [

    # StudentLogin API
    path('api/StudentLogin/', StudentLoginApiView.as_view()),

    # Course API
    path('api/course/', CourseApiView.as_view()),
    path('api/course/detail/<int:C_id>/', CourseDetail.as_view()),

    # Teacher API
    path('api/teacher/', TeacherApiView.as_view()),
    path('api/teacher/detail/<int:T_id>/', TeacherDetail.as_view()),

    # Student API
    path('api/student/', StudentApiView.as_view()),
    path('api/student/detail/<int:S_id>/', StudentDetail.as_view()),

    # Sign API
    path('api/sign/', SignApiView.as_view()),
    path('api/sign/detail/<int:Sign_id>/', SignDetail.as_view()),

    # Race_Answer API
    path('api/race_answer/', Race_AnswerApiView.as_view()),
    path('api/race_answer/detail/<int:R_id>/', Race_AnswerDetail.as_view()),

    # Race_List API
    path('api/race_list/', Race_ListApiView.as_view()),
    path('api/race_list/detail/<int:Time>/', Race_ListDetail.as_view()),

    # Sign_Record API
    path('api/sign_record/', Sign_RecordApiView.as_view()),
    path('api/sign_record/detail/<int:SR_id>/', Sign_RecordDetail.as_view()),

    # Team API
    path('api/team/', TeamApiView.as_view()),
    path('api/team/detail/<int:Team_id>/', TeamDetail.as_view()),

    # Team_Desc API
    path('api/team_desc/', Team_DescApiView.as_view()),
    path('api/team_desc/detail/<int:TeamDesc_id>/', Team_DescDetail.as_view()),

    # Team_Member API
    path('api/team_member/', Team_MemberApiView.as_view()),
    path('api/team_member/detail/<int:TeamMember_id>/', Team_MemberDetail.as_view()),
]
