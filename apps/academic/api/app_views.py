from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter

from apps.academic import choices
from apps.academic.api import app_serializers
from rest_framework import serializers
from apps.academic.models import Exam, ExamQuestion, AnswerExame, ExamQuestionOption, AnswerExamQuestion
from django_filters import rest_framework as filters
from django.utils.translation import gettext as _


class IsValidationTokenApi(permissions.BasePermission):
    # Regras de validação/permissão/Autenticação
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return True


class AcademicModuleMinx:
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsValidationTokenApi,)

    def validate_status_exam(self, instance):
        if instance.status != choices.ACTIVATE:
            raise serializers.ValidationError(
                _('O exame só pode ser acessado se estiver ativo.')
            )


class ExamAPIListView_V1(AcademicModuleMinx, generics.ListAPIView):
    serializer_class = app_serializers.AcademicSerializer_V1
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering = ('id',)
    search_fields = ('title', 'status',)
    queryset = Exam.objects.all()


class ExamAPIDetailView_V1(AcademicModuleMinx, generics.RetrieveAPIView):
    serializer_class = app_serializers.AcademicDetailSerializer_V1
    queryset = Exam.objects.all()

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        self.validate_status_exam(object)
        # Ao acessar um exame ativo, é criado uma resposta para esse exame.
        answer = object.answer.filter(user=request.user).first()
        if not answer:
            AnswerExame.objects.create(**dict(
                user=request.user,
                exam=object,
            ))
        return self.retrieve(request, *args, **kwargs)


class ExamQuestionAPIDetailView_V1(AcademicModuleMinx, generics.RetrieveAPIView, generics.CreateAPIView):
    serializer_class = app_serializers.ExamQuestionSerializer_V1
    queryset = ExamQuestion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return app_serializers.ExamQuestionSerializer_V1
        if self.request.method == 'POST':
            return app_serializers.AnswerExamQuestionPostSerializer_V1

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        self.validate_status_exam(object.exam)
        return self.retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        exame = get_object_or_404(Exam, pk=kwargs.get('pk_exame'))
        question = get_object_or_404(ExamQuestion, pk=kwargs.get('pk'))
        option = get_object_or_404(ExamQuestionOption, pk=request.data.get('pk_option_question'))
        # só existe 1 answerExame para o exame e o usuário
        answer = exame.answer.filter(user=request.user).first()
        _, _ = AnswerExamQuestion.objects.get_or_create(**dict(
            answer=answer,
            question=question,
            options=option,
            is_correct=option.is_correct
        ))
        serializer = app_serializers.ExamQuestionSerializer_V1(question, context=self.get_serializer_context())
        return Response(serializer.data, status=status.HTTP_201_CREATED, )

    def put(self, request, *args, **kwargs):
        exame = get_object_or_404(Exam, pk=kwargs.get('pk_exame'))
        answer = exame.answer.filter(user=request.user).first()
        answer.status = choices.FINISHED
        answer.save()
        return Response(status=status.HTTP_202_ACCEPTED)
