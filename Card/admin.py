from django.contrib import admin
from Card.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'list', 'priority', 'status')
    filter = ('title', 'status')
    search_fields = ('title', 'status')
