from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from blog.models import BlogPage
from projects.models import ProjectPage
from streams.blocks import SkillsAndToolsBlock


class HomePage(Page):
    body = RichTextField(blank=True)
    hero_title = models.CharField(
        max_length=120,
        blank=True,
        help_text="Main text displayed in the hero section over the background."
    )
    hero_subtitle = models.CharField(
        max_length=300,
        blank=True,
        help_text="Subtitle text for the hero section."
    )
    hero_photo = models.ImageField(
        blank=True,
        help_text="Image of me to be displayed in the hero."
    )
    skills_and_tools = StreamField([
        ('skills_and_tools', SkillsAndToolsBlock())
    ], blank=True)

    # Configure the Admin interface
    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_subtitle"),
        FieldPanel('hero_photo'),
        FieldPanel('body', classname="full"),
        StreamFieldPanel('skills_and_tools'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        projects = ProjectPage.objects.live()
        context['projects'] = projects
        return context