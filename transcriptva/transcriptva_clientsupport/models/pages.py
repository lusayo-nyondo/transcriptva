from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index


class RootPage(Page):
    pass


class SupportIndex(Page):
    template = 'transcriptva_clientsupport/index.dtl.html'
    
    body = RichTextField()

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    subpage_types = [
        'transcriptva_clientsupport.SupportArticle'
    ]


class SupportArticle(Page):
    template = 'transcriptva_clientsupport/support_article.dtl.html'

    body = RichTextField()
    date = models.DateField("Post date")

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('image'),
        FieldPanel('date'),
        FieldPanel('body'),
        
        InlinePanel('related_links', heading="Related links", label="Related link")
    ]

    parent_page_types = [
        'transcriptva_clientsupport.SupportIndex',
        'transcriptva_clientsupport.SupportArticle',
    ]

    subpage_types = [
        'transcriptva_clientsupport.SupportArticle'
    ]


class SupportArticleRelatedLink(Orderable):
    page = ParentalKey(
        SupportArticle,
        on_delete=models.CASCADE,
        related_name='related_links'
    )

    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]
