from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.academic.models import AnswerExamQuestion, Exam


@receiver(post_save, sender=AnswerExamQuestion)
def pre_save_exam_quetions_options(sender, instance, raw, using, *args, **kwargs):
    instance.answer.calculate_scores()
