# Generated by Django 4.2.11 on 2024-05-09 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moru', '0004_htels_content2_htels_content3_htels_content4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htels',
            name='content2',
            field=models.CharField(max_length=100000000, null=True),
        ),
        migrations.AlterField(
            model_name='htels',
            name='content3',
            field=models.CharField(max_length=100000000, null=True),
        ),
        migrations.AlterField(
            model_name='htels',
            name='content4',
            field=models.CharField(max_length=100000000, null=True),
        ),
        migrations.AlterField(
            model_name='htels',
            name='content5',
            field=models.CharField(max_length=100000000, null=True),
        ),
        migrations.AlterField(
            model_name='htels',
            name='content6',
            field=models.CharField(max_length=100000000, null=True),
        ),
    ]