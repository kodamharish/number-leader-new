# Generated by Django 5.1 on 2024-09-18 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_forecastingcashflow_month_or_quarter_or_year_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='company_ask',
            new_name='Ask',
        ),
        migrations.RenameField(
            model_name='ask',
            old_name='company_id',
            new_name='company',
        ),
    ]
