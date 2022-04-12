from django.contrib import admin
from Board.models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'visibility', 'workspace')
    search_fields = ('title',)
    filter = ('workspace', 'title', 'visibility')
