from django.contrib import admin
from Cart_items.models import (
    Label,
    List,
    Checklist,
    Template,
    Item,
)


@admin.register(Label)
class LAbelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('title',)
