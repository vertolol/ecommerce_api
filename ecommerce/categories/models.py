from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from autoslug import AutoSlugField
from products.models import Product
from django.urls import reverse
from django.contrib.postgres.fields import JSONField


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='name')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    attributes = JSONField(blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    @property
    def parent_link(self):
        return self.parent.link

    @property
    def link(self):
        return reverse('category_detail',
                       kwargs={'slug': self.slug})

    @property
    def children_node_info(self):
        children_node = Category.objects.add_related_count(self.get_children(),
                                                      Product,
                                                      'category',
                                                      'pr_count',
                                                      cumulative=True)
        return [{'link': ch.link, 'name': ch.name, 'count': ch.pr_count} for ch in children_node]
