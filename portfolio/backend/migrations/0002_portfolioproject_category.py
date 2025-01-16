# Generated by Django 5.1.4 on 2025-01-16 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioproject',
            name='category',
            field=models.CharField(choices=[('fashion', 'Fashion'), ('nature', 'Nature'), ('wedding', 'Wedding'), ('product', 'Product'), ('studio', 'Studio'), ('sports', 'Sports')], default='fashion', max_length=50),
        ),
    ]