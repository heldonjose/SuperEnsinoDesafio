from django.utils.translation import gettext as _

DRAFT = 'draft'
ACTIVATE = 'active'
OPEN = 'open'
FINISHED = 'finished'

STATUS_EXAME = [
    (DRAFT, _(u'Rascunho')),
    (ACTIVATE, _(u'Ativo')),
]

STATUS_ANSWER = [
    (OPEN, _(u'Aberta')),
    (FINISHED, _(u'Finalizada')),
]
