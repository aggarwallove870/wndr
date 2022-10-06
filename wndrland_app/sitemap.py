from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from  .models import *

class StaticViewSitemap(Sitemap):
    changefreq='weekly'
    priority = 0.7
    protocol ='https'
    def items(self):
        return ['home','about','vision','contact','teams']
    def location(self, item):
        return reverse(item)