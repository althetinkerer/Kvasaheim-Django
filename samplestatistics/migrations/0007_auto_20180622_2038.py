# Generated by Django 2.0.1 on 2018-06-23 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samplestatistics', '0006_auto_20180622_1907'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='problem',
            name='excel',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='formula',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='rcode',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='solution',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
