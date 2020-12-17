from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from events.models import EventsPluginModel
from django.utils.translation import gettext as _

class EventsItemPlugin(CMSPluginBase):
    model = EventsPluginModel  
    module = _("Events")
    name = _("Featured Events Item")
    render_template = "events/plugin-child.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

class FeaturedEventsPlugin(CMSPluginBase):
    module = _("Events")
    name = _("Featured Events")
    render_template = "events/plugin-parent.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(EventsItemPlugin)
plugin_pool.register_plugin(FeaturedEventsPlugin)