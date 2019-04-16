from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import Partner, TeamMember, Project

@plugin_pool.register_plugin
class PartnersPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Partners Plugin")
    render_template = "partner_list.html"
    cache = False

    def render(self, context, instance, placeholder):
        context['partners'] = Partner.objects.order_by('position')
        return context

@plugin_pool.register_plugin
class MembersPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Members Plugin")
    render_template = "member_list.html"
    cache = False

    def render(self, context, instance, placeholder):
        context['active_members'] = TeamMember.objects.filter(is_active=True, is_lab_affiliate=False).order_by('position')
        context['lab_affiliate_members'] = TeamMember.objects.filter(is_active=True, is_lab_affiliate=True).order_by('position')
        context['inactive_members'] = TeamMember.objects.filter(is_active=False).order_by('position')
        return context


@plugin_pool.register_plugin
class SeparatorPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Separator")
    render_template = "separator.html"
    cache = False

    def render(self, context, instance, placeholder):
        return context

@plugin_pool.register_plugin
class ProjectsActivePlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Current Projects")
    render_template = "project_active_list.html"
    cache = False

    def render(self, context, instance, placeholder):
        context['active_projects'] = Project.objects.order_by('position').filter(is_active=True)
        return context

@plugin_pool.register_plugin
class ProjectsInactivePlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Past Projects")
    render_template = "project_inactive_list.html"
    cache = False

    def render(self, context, instance, placeholder):
        context['inactive_projects'] = Project.objects.order_by('position').filter(is_active=False)
        return context