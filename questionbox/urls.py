from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from questionboard import views
from django.contrib.auth import views as auth_views


router = DefaultRouter()
router.register(r'api/question', views.QuestionViewSet)
router.register(r'api/answer', views.AnswerViewSet)
router.register(r'api/users', views.UserViewSet)

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^question/$', views.user_question, name='user_questions'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name='questions'),

]
