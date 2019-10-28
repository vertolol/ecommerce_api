# Generated by Django 2.2.6 on 2019-10-28 08:31

import autoslug.fields
import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('price', models.IntegerField()),
                ('attributes', django.contrib.postgres.fields.jsonb.JSONField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='categories.Category')),
            ],
        ),
        migrations.AddIndex(
            model_name='product',
            index=django.contrib.postgres.indexes.GinIndex(fields=['attributes'], name='json_index', opclasses=['jsonb_path_ops']),
        ),
    ]