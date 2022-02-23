from django.urls import path, include,re_path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views
from .views import *

router = DefaultRouter()
router.register('StudentLogin', StudentLoginViewSet)
router.register('Student', StudentViewSet)
router.register('TeacherLogin', TeacherLoginViewSet)
router.register('CourseCreate', CourseViewSet)
router.register('CourseRecord', CourseRecordViewSet)
router.register('Sign', SignViewSet)
router.register('SignRecord', SignRecordViewSet)
router.register('Race_List', Race_ListViewSet)
router.register('Race_Answer', Race_AnswerViewSet)
router.register('Race_List_R', Race_List_R_ViewSet)
router.register('Team_Desc', Team_DescViewSet)
router.register('Team', TeamViewSet)
router.register('Team_Member', Team_MemberViewSet)
router.register('QA_Topic', QA_TopicViewSet)
router.register('Question', QuestionViewSet)
router.register('Question_Q', Question_QViewSet)
router.register('Answer_Member', Answer_MemberViewSet)


urlpatterns = [

    path('api/', include(router.urls)),

    #後臺網頁
    path('',views.login,name="login"),
    path('user_login/',views.user_login,name="user_login"),

]
