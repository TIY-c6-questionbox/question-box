from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from questionboard import views
from django.contrib.auth import views as auth_views


router = DefaultRouter()
router.register(r'question', views.QuestionViewSet)
router.register(r'answer', views.AnswerViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^index', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
