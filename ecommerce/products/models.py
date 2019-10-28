from django.contrib.postgres.indexes import GinIndex
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.postgres.fields import JSONField


class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from='name', unique=True)
    price = models.IntegerField()
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='product')
    attributes = JSONField()

    class Meta():
        indexes = [GinIndex(name='json_index', fields=['attributes'], opclasses=['jsonb_path_ops'])]

    def __str__(self):
        return self.name

    @property
    def link(self):
        return reverse('product:product-detail', kwargs={'slug': self.slug})
