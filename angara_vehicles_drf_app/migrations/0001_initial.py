# Generated by Django 5.0 on 2023-12-07 21:54

import django.db.models.deletion
import django.utils.timezone
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=4, default=Decimal('0.00'), max_digits=19)),
                ('weight', models.BigIntegerField()),
                ('city_production', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('image_path', models.TextField()),
                ('manufacturing_ccompany', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(1, 'Удален'), (2, 'Действует')])),
                ('component_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('engine_name', models.CharField(blank=True, max_length=255, null=True)),
                ('total_thrust', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('dry_weight', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('combustion_chamber_pressure', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
            ],
            options={
                'verbose_name_plural': 'Components',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=30, null=True)),
                ('adress', models.CharField(max_length=400, null=True)),
                ('is_moderator', models.BooleanField()),
                ('login', models.CharField(max_length=255)),
                ('passwd', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Черновик'), (2, 'Удален'), (3, 'Сформирован'), (4, 'Завершен'), (5, 'Отклонен')])),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('formation_date', models.DateTimeField(blank=True, null=True)),
                ('completion_date', models.DateTimeField(blank=True, null=True)),
                ('id_creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='angara_vehicles_drf_app.users')),
                ('id_moderator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications_customer_set', to='angara_vehicles_drf_app.users')),
            ],
            options={
                'verbose_name_plural': 'Applications',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ApplicationsComponents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('components_amount', models.IntegerField()),
                ('id_application', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='angara_vehicles_drf_app.applications')),
                ('id_component', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='angara_vehicles_drf_app.components')),
            ],
            options={
                'managed': True,
                'unique_together': {('id_component', 'id_application')},
            },
        ),
    ]
