from django.db import models
from Workspace.models import Workspace
from django.utils.translation import gettext_lazy as _
from Common.models import BaseModel


class Board(BaseModel):
    class Visibility(models.TextChoices):
        PRIVATE = 'PR', _('Private')
        WORKSPACE = 'WS', _('Workspace')
        PUBLIC = 'PB', _('Public')

    class Background(models.TextChoices):
        BL = 'Blue'
        OR = 'Orange'
        GN = 'Green'
        RD = 'Red'
        PL = 'Purple'
        PK = 'Pink'
        LM = 'Lime'
        SY = 'Sky'
        GY = 'Gray'

    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE,
                                  related_name='boards', verbose_name='Workspaces of Board')
    member = models.ManyToManyField('Accounts.User', related_name='boards')
    title = models.CharField('Title', max_length=100)
    visibility = models.CharField('Visibility', max_length=100, choices=Visibility.choices,
                                  default='Workspace', )
    background = models.CharField('Background Color', max_length=100, choices=Background.choices, default='Gray')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'
