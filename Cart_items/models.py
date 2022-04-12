from django.db import models
from Common.models import BaseModel


class List(BaseModel):
    board = models.ForeignKey('Board.Board', on_delete=models.CASCADE,
                              related_name='lists', verbose_name='lists of the board')
    title = models.CharField(max_length=100, verbose_name='Title')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'List'
        verbose_name_plural = 'Lists'


class Template(BaseModel):
    card = models.ForeignKey('Card.Card', on_delete=models.SET_NULL,
                             null=True, related_name='templates')
    title = models.TextField()
    photo = models.ImageField(upload_to='images/templates')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'


class Label(BaseModel):
    Color_Type = (
        (1, 'Green'),
        (2, 'Yellow'),
        (3, 'Orange'),
        (4, 'Red'),
        (5, 'Pink'),
        (6, 'Blue'),
    )
    card = models.ForeignKey('Card.Card', on_delete=models.SET_NULL, null=True,
                             related_name='labels', verbose_name='cards of a label')
    name = models.CharField(max_length=100)
    color_type = models.CharField(choices=Color_Type, max_length=100, verbose_name='Color types of Label')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Label'
        verbose_name_plural = 'Labels'
        ordering = ('card', 'name')


class Checklist(BaseModel):
    card = models.ForeignKey('Card.Card', on_delete=models.SET_NULL,null=True, related_name='checklists',
                             verbose_name='checklists of a card')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Checklist'



class Item(BaseModel):
    checklist = models.ForeignKey('Cart_items.Checklist', on_delete=models.CASCADE,
                                  related_name='items', verbose_name='items of a checklist')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ('created_at', 'updated_at')
