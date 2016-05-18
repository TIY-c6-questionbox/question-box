from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from questionbox import views


router = routers.DefaultRouter()
router.register(r'question', views.QuestionViewSet)
router.register(r'answer', views.AnswerViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'questionbox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', include(admin.site.urls)),
]
