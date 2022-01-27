from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from apps.academic import choices
from django.db import models

from apps.core.models import TimeStampableMixin as TimeMixin


class Exam(TimeMixin):
    class Meta:
        verbose_name = _(u'Exame')
        verbose_name_plural = _(u'Exames')

    title = models.CharField(_('Título'), max_length=255)
    status = models.CharField(_(u'Situação'), max_length=20, choices=choices.STATUS_EXAME, default='open')

    def __str__(self):
        return str(self.title)


class ExamQuestion(models.Model):
    class Meta:
        verbose_name = _(u'Questão do exame')
        verbose_name_plural = _(u'Questões dos exames')

    exam = models.ForeignKey(Exam, verbose_name=_(u'Exame'), on_delete=models.CASCADE, related_name='questions')
    title = models.TextField(_(u'Título'))
    is_single_choice = models.BooleanField(_(u'É de escolha única?'), default=True)

    def __str__(self):
        return str(self.title)


class ExamQuestionOption(models.Model):
    class Meta:
        verbose_name = _(u'Opção de questão de exame')
        verbose_name_plural = _(u'Opções de questões de exames')

    question = models.ForeignKey(ExamQuestion, verbose_name=_(u'Questão'), on_delete=models.CASCADE, related_name='options')
    text = models.TextField(_(u'Texto da opção'))
    is_correct = models.BooleanField(_(u'É uma opção correta?'), default=False)

    def __str__(self):
        return str(self.text)


class AnswerExame(TimeMixin):
    class Meta:
        verbose_name = _(u'Resposta do Exame')
        verbose_name_plural = _(u'Respostas dos Exames')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_(u'Usuário'), related_name='answers')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='answer')
    sent_at = models.DateTimeField(_(u'Dt. de envio'), blank=True, null=True)
    status = models.CharField(_(u'Situação'), max_length=20, choices=choices.STATUS_ANSWER, default='open')
    total_correct = models.PositiveIntegerField(_('Total de acertos'), default=0)
    total_erros = models.PositiveIntegerField(_('Total de erros'), default=0)
    percentage_correct = models.DecimalField(_('Aproveitamento'), max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return str(self.exam)

    def calculate_scores(self):
        total = self.exam.questions.all()
        self.total_correct = self.answersquestions.filter(is_correct=True).count()
        self.total_erros = self.answersquestions.filter(is_correct=False).count()
        self.percentage_correct = round((self.total_correct/total.count())*100, 2)
        self.save()

class AnswerExamQuestion(models.Model):
    class Meta:
        verbose_name = _(u'Resposta de questão do Exame')
        verbose_name_plural = _(u'Respostas de questões de avaliações dos cursos')

    answer = models.ForeignKey(AnswerExame, on_delete=models.CASCADE, verbose_name=_(u'Resposta do exame'), related_name='answersquestions')
    question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE, verbose_name=_(u'Resposta da questão do exame'), related_name='answersquestions')
    options = models.ForeignKey(ExamQuestionOption, on_delete=models.CASCADE, verbose_name=_(u'Opção da questão do exame'), related_name='answersquestions')
    is_correct = models.BooleanField(_(u'A resposta está correta?'), default=False)

    def __str__(self):
        return str(self.question)
