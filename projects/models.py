from django.db import models

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
    """Project page class."""

    template = 'projects/project_page.html'

    class Meta:
        verbose_name = "Project Page"
        verbose_name_plural = "Project Pages"
