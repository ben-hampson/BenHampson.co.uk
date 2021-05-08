"""Streamfields live here."""

from wagtail.core import blocks

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