from django.db import models
from django.utils.translation import gettext_lazy as _
from Common.models import BaseModel
from Cart_items.models import List


class Card(BaseModel):
    class Priority(models.TextChoices):
        HIGHEST = 'HS', _('Highest')
        HIGH = 'HG', _('High')
        MEDIUM = 'MI', _('Medium')
        LOW = 'LW', _('Low')
        LOWEST = 'LS', _('Lowest')

    class STATUS(models.TextChoices):
        TO_DO = 'TD', _('To Do')
        IN_PROGRESS = 'IP', _('In progress')
        DONE = 'DN', _('Done')
        IN_REVIEW = 'IR', _('In review')
        APPROVED = 'AR', _('Approved')
        NOT_SURE = 'NS', _('Not sure')

    list = models.ForeignKey('Cart_items.List', on_delete=models.CASCADE,
                             related_name='cards', verbose_name='cards of a list')
    member = models.ManyToManyField('Accounts.User', related_name='cards')
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    priority = models.CharField(max_length=100, choices=Priority.choices,
                                verbose_name='priorities of Card')
    status = models.CharField(max_length=100, choices=STATUS.choices,
                              verbose_name='status of card')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
        ordering = ('title',)

