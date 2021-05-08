from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from flex.models import FlexPage

class ProjectIndexPage(FlexPage):
    def get_context(self, request):
        context = super().get_context(request)
        projectpages = self.get_children().live().order_by('-first_published_at')
        context['projectpages'] = projectpages
        return context

    class Meta:
        verbose_name = "Project Index Page"
        verbose_name_plural = "Project Index Pages"

class ProjectPage(FlexPage):
    """Project page model."""

    template = 'projects/project_page.html'

    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True, 
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = FlexPage.content_panels + [
        ImageChooserPanel("banner_image"),
    ]

    class Meta:
        verbose_name = "Project Page"
        verbose_name_plural = "Project Pages"
