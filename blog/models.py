
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from tagging.models import Tag
from tagging.fields import TagField

class Post(models.Model):
    title = models.CharField(_("title"), max_length=100)
    slug = models.SlugField(_("slug"), unique=True, prepopulate_from=("title",))
    body = models.TextField(_("body"))
    create_date = models.DateTimeField(_("created"), default=datetime.now)
    pub_date = models.DateTimeField(_("published"), default=datetime.now)
    tags = TagField()
    
    def __unicode__(self):
        return self.title
    
    class Admin:
        list_display = ("id", "title", "pub_date")
        list_display_links = ("id", "title")
        search_fields = ("title", "text")
    
    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ("-pub_date",)
    
    def get_absolute_url(self):
        return ("blog_post_detail", (), {
            "year": self.pub_date.strftime("%Y"),
            "month": self.pub_date.strftime("%b").lower(),
            "day": self.pub_date.strftime("%d"),
            "slug": self.slug,
        })
    get_absolute_url = models.permalink(get_absolute_url)