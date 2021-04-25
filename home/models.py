from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


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

    # Configure the Admin interface
    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_subtitle"),
        FieldPanel('body', classname="full"),
    ]