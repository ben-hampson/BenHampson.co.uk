"""Streamfields live here."""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features"""
    features = ['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'image', 'code', 'blockquote']

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Full RichText"

class FeaturesAndToolsBlock(blocks.StructBlock):
    """Features of a project and tools used to build it."""

    features = blocks.RichTextBlock(required=False, help_text="List the features")
    tools = blocks.RichTextBlock(required=False, help_text="List the tools")

    class Meta:
        template = "streams/features_and_tools_block.html"
        icon = "edit"
        label = "Features & Tools"

class SkillsAndToolsBlock(blocks.StructBlock):
    """Showcase my skills and tools."""

    title = blocks.CharBlock(required=False, help_title="Add a title")

    skills = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=False)),
                ("title", blocks.CharBlock(required=False, max_length=100))
            ]
        )
    )

    class Meta:
        template = "streams/skills_and_tools_block.html"
        icon = "edit"
        label = "Skills & Tools"