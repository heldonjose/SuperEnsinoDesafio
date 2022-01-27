from django.utils.translation import gettext as _
from rest_framework import serializers

from apps.academic import choices
from apps.academic.models import Exam, ExamQuestion, ExamQuestionOption, AnswerExamQuestion, AnswerExame


class AcademicSerializer_V1(serializers.ModelSerializer):
    has_answers = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = [field.name for field in model._meta.fields] + ['has_answers']

    def get_has_answers(self, obj):
        answer = obj.answer.filter(user=self.context.get('request').user).first()
        return answer and answer.status == choices.FINISHED


class ExamQuestionOptionSerializer_V1(serializers.ModelSerializer):
    class Meta:
        model = ExamQuestionOption
        exclude = ('question',)


class AnswerExamQuestionPostSerializer_V1(serializers.ModelSerializer):
    pk_option_question = serializers.IntegerField()

    class Meta:
        model = AnswerExamQuestion
        fields = ('pk_option_question',)


class AnswerExamSerializer_V1(serializers.ModelSerializer):
    class Meta:
        model = AnswerExame
        exclude = ('user',)


class ExamQuestionSerializer_V1(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    has_option_answer = serializers.SerializerMethodField()

    class Meta:
        model = ExamQuestion
        fields = ('id', 'title', 'is_single_choice', 'options', 'has_option_answer')

    def get_options(self, obj):
        return ExamQuestionOptionSerializer_V1(obj.options.all(), many=True, context=self.context).data

    def get_has_option_answer(self, obj):
        # só existe 1 answerExame para o exame e o usuário
        answer = obj.exam.answer.filter(user=self.context.get('request').user).first()
        # só existe 1 answerExameQuestion para o answer e a question
        answer_question = answer.answersquestions.filter(question=obj).first()
        return {'option': answer_question.options.pk, 'is_correct': answer_question.is_correct} if answer_question else False


class AcademicDetailSerializer_V1(AcademicSerializer_V1):
    questions = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta(AcademicSerializer_V1.Meta):
        fields = AcademicSerializer_V1.Meta.fields + ['questions', 'answer']

    def get_questions(self, obj):
        return ExamQuestionSerializer_V1(obj.questions.all(), many=True, context=self.context).data

    def get_answer(self, obj):
        if self.get_has_answers(obj):
            answer = obj.answer.filter(user=self.context.get('request').user).first()
            return AnswerExamSerializer_V1(answer).data
        return _('O Exame ainda não foi finalizado')
