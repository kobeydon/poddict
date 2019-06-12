from django import template
import markdown
from markdownx.settings import (
MARKDOWNX_MARKDOWN_EXTENSIONS,
MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS
)
from markdown.extensions import Extension
from django.utils.safestring import mark_safe

register = template.Library()

class EscapeHtml(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.deregister('html_block')
        md.inlinePatterns.deregister('html')

@register.filter
def markdown_to_html_with_escape(text):
    """convert markdown to html except for raw CSS, JS, HTML"""

    extensions = MARKDOWNX_MARKDOWN_EXTENSIONS + [EscapeHtml()]
    html = markdown.markdown(text, extensions=extensions, extension_config=MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS)
    return mark_safe(html)