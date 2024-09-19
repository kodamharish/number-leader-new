# Generated by Django 5.0.4 on 2024-08-14 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_company_subscription_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='founder',
            name='date_joined',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='founder',
            name='photo',
            field=models.ImageField(null=True, upload_to='founder_photos'),
        ),
        migrations.CreateModel(
            name='company_ask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.IntegerField(null=True)),
                ('valuation', models.IntegerField(null=True)),
                ('equity_share', models.DecimalField(decimal_places=1, max_digits=5, null=True)),
                ('details', models.TextField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
