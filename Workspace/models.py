from django.db import models
from django.utils.translation import gettext_lazy as _


def default_category():
    return {'choice a category': 'choice a category'}


class Workspace(models.Model):
    class CategoryType(models.TextChoices):
        POPULAR = 'PL', _('POPULAR')
        SMALL_BUSINESS = 'SM', _('SMALL BUSINESS')
        DESIGN = 'DS', _('DESIGN')
        EDUCATION = 'ED', _('EDUCATION')
        ENGINEERING_IT = 'EI', _('ENGINEERING IT')
        MARKETING = 'MK', _('MARKETING')
        HUMAN_RESOURCES = 'HR', _('HUMAN RESOURCES')
        OPERATIONS = 'OP', _('OPERATIONS')
        SALES_CRM = 'SC', _('SALES CRM')

    member = models.ForeignKey('Accounts.User', on_delete=models.SET_NULL, null=True, related_name='workspaces',
                               verbose_name='members of workspace')
    title = models.CharField('Name', max_length=100)
    photo = models.ImageField('Photo', 'upload_to')
    description = models.TextField('Description')
    category_type = models.CharField(choices=CategoryType.choices, max_length=100,
                                     default=default_category, verbose_name='Category Types')
    website = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Workspace'
        verbose_name_plural = 'Workspaces'
