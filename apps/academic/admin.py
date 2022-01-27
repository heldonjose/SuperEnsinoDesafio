from django.contrib import admin, messages

# Register your models here.
from django import forms
from django.core.exceptions import ValidationError
from nested_admin.nested import NestedStackedInline, NestedModelAdmin, NestedTabularInline

from apps.academic import choices
from apps.academic.models import Exam, ExamQuestion, ExamQuestionOption, AnswerExame, AnswerExamQuestion


class ExamQuestionOptionInline(NestedTabularInline):
    model = ExamQuestionOption
    extra = 0


class ExamQuestionInline(NestedStackedInline):
    model = ExamQuestion
    extra = 0
    inlines = (ExamQuestionOptionInline,)


class ExamAdminForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        if not self.instance.pk and status != choices.DRAFT:
            self.add_error('status', u'Na criação de um exame o status deverá sempre ser Rascunho')
        if self.instance.pk and status == choices.ACTIVATE:
            if not self.instance.questions.exists():
                self.add_error('status', 'Não existem questões salva para esse exame, save todas as quesõtes com o exame ainda em rascunho')
            for question in self.instance.questions.all():
                if not question.options.exists():
                    self.add_error('status', 'Existem questões sem opções, por favor, crie pelo menos uma opção para cada questão')
                else:
                    print('==', question.options.filter(is_correct=True))
                    if question.options.filter(is_correct=True).count() != 1:
                        self.add_error('status', 'Só poderá ter uma opção correta para cada questões, salve o exame como rascunho antes de mudar o status')
        return cleaned_data


@admin.register(Exam)
class ExamAdmin(NestedModelAdmin):
    form = ExamAdminForm
    list_filter = ('status',)
    list_display = ('title', 'status',)
    search_fields = ('title',)
    inlines = (ExamQuestionInline,)


@admin.register(AnswerExame)
class AnswerExameAdmin(NestedModelAdmin):
    list_filter = ('exam',)
    list_display = [field.name for field in AnswerExame._meta.fields]


@admin.register(AnswerExamQuestion)
class AnswerExamQuestionAdmin(NestedModelAdmin):
    list_filter = ('answer',)
    list_display = [field.name for field in AnswerExamQuestion._meta.fields]
