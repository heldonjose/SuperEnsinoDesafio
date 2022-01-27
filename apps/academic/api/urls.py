from django.urls import re_path

from apps.academic.api import app_views

urlpatterns = [
    # EXAME
    re_path(r'^(?P<version>(v1))/exame/?$', app_views.ExamAPIListView_V1.as_view()),
    re_path(r'^(?P<version>(v1))/exame/(?P<pk>[0-9]+)/?$', app_views.ExamAPIDetailView_V1.as_view()),
    re_path(r'^(?P<version>(v1))/exame/(?P<pk_exame>[0-9]+)/question/(?P<pk>[0-9]+)/?$', app_views.ExamQuestionAPIDetailView_V1.as_view()),

]
