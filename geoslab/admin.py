from django.contrib import admin
from .models import Partner, TeamMember, Project\
	# , ImageProject


class PartnerAdmin(admin.ModelAdmin):
  list_display = ('name', 'is_active', 'position')

class TeamMemberAdmin(admin.ModelAdmin):
  list_display = ('name', 'is_active', 'position')
  
class ProjectAdmin(admin.ModelAdmin):
  list_display = ('name', 'is_active', 'position')
	
# Register your models here.
admin.site.register(Partner, PartnerAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Project, ProjectAdmin)
# admin.site.register(ImageProject)
