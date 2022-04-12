from django.contrib import admin
from Workspace.models import Workspace


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_type')
    search_fields = ('title',)
