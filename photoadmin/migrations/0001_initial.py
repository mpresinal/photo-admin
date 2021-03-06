# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 14:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(db_column='address_id', primary_key=True, serialize=False)),
                ('address', models.CharField(db_column='address', max_length=220)),
                ('zip_code', models.CharField(db_column='zip_code', max_length=20)),
                ('city', models.CharField(db_column='city', max_length=100)),
                ('state', models.CharField(db_column='state', max_length=100)),
                ('country', models.CharField(db_column='country', max_length=100)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(db_column='person_id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=60)),
                ('last_name', models.CharField(db_column='last_name', max_length=60)),
                ('birthday', models.DateField(blank=True, db_column='birthday', null=True)),
                ('phone', models.CharField(blank=True, db_column='phone', max_length=30, null=True)),
                ('gender', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], db_column='gender', max_length=5)),
                ('cell_phone', models.CharField(db_column='cell_phone', max_length=30)),
                ('email', models.EmailField(db_column='email', max_length=100)),
                ('facebook', models.CharField(blank=True, db_column='facebook', max_length=100, null=True)),
                ('whatsapp', models.CharField(blank=True, db_column='whatsapp', max_length=30, null=True)),
                ('address', models.ForeignKey(db_column='address_id', on_delete=django.db.models.deletion.PROTECT, to='photoadmin.Address')),
                ('user', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(db_column='photographer_id', primary_key=True, serialize=False)),
                ('water_mark_file', models.ImageField(blank=True, db_column='water_mark_file', null=True, upload_to='photographer/watermarks')),
                ('person', models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, to='photoadmin.Person')),
            ],
            options={
                'db_table': 'photographer',
            },
        ),
        migrations.CreateModel(
            name='PhotographerPhotoPrinting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('photographer_code', models.CharField(db_column='photo_printing_code', max_length=10)),
                ('photographer', models.ForeignKey(db_column='photographer_id', on_delete=django.db.models.deletion.CASCADE, related_name='photographer_photoprinting', to='photoadmin.Photographer')),
            ],
            options={
                'db_table': 'photographer_photo_printing',
            },
        ),
        migrations.CreateModel(
            name='PhotoPrinting',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(db_column='photo_printing_id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=100)),
                ('phone', models.CharField(db_column='phone', max_length=30)),
                ('email', models.EmailField(blank=True, db_column='email', max_length=100)),
                ('contact_name', models.CharField(db_column='contact_name', max_length=100)),
                ('contact_phone', models.CharField(db_column='contact_phone', max_length=30)),
                ('contact_email', models.EmailField(db_column='contact_email', max_length=100)),
                ('address_street', models.CharField(db_column='street', max_length=200)),
                ('address_zip_code', models.CharField(db_column='zip_code', max_length=20)),
                ('address_city', models.CharField(db_column='city', max_length=100)),
                ('address_state', models.CharField(db_column='state', max_length=100)),
                ('address_country', models.CharField(db_column='country', max_length=100)),
                ('address_location', models.CharField(db_column='location', max_length=200, null=True)),
                ('photographers', models.ManyToManyField(through='photoadmin.PhotographerPhotoPrinting', to='photoadmin.Photographer')),
            ],
            options={
                'db_table': 'photo_printing',
            },
        ),
        migrations.CreateModel(
            name='PhotoShoot',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(db_column='photo_shoot_id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=100)),
                ('description', models.CharField(blank=True, db_column='description', max_length=256, null=True)),
                ('capture_time', models.DateTimeField(db_column='capture_time')),
                ('photographer', models.ForeignKey(db_column='photographer_id', on_delete=django.db.models.deletion.CASCADE, to='photoadmin.Photographer')),
            ],
            options={
                'db_table': 'photo_shoot',
            },
        ),
        migrations.CreateModel(
            name='PhotoShootPhoto',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(db_column='photo_shoot_photo_id', primary_key=True, serialize=False)),
                ('photo_file', models.ImageField(db_column='file', upload_to='')),
                ('file_dir', models.CharField(blank=True, db_column='directory', max_length=200)),
                ('file_size', models.IntegerField(blank=True, db_column='file_size')),
                ('photo_shoot_id', models.ForeignKey(db_column='photo_shoot_id', on_delete=django.db.models.deletion.CASCADE, to='photoadmin.PhotoShoot')),
            ],
            options={
                'db_table': 'photo_shoot_photo',
            },
        ),
        migrations.CreateModel(
            name='PhotoShootSelection',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(db_column='photo_shoot_selection_id', primary_key=True, serialize=False)),
                ('print_after_confirmation', models.BooleanField(db_column='print_after_confirmation')),
                ('photo_printing_id', models.BigIntegerField(db_column='photo_printing_id')),
                ('person', models.ForeignKey(blank=True, db_column='person_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='photoadmin.Person')),
            ],
            options={
                'db_table': 'photo_shoot_selection',
            },
        ),
        migrations.CreateModel(
            name='PhotoStudio',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(db_column='photo_studio_id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=100)),
                ('street', models.CharField(db_column='street', max_length=200)),
                ('zip_code', models.CharField(db_column='zip_code', max_length=20)),
                ('city', models.CharField(db_column='city', max_length=100)),
                ('state', models.CharField(db_column='state', max_length=100)),
                ('country', models.CharField(db_column='country', max_length=100)),
                ('location', models.CharField(db_column='location', max_length=200)),
                ('photographer', models.ForeignKey(db_column='photographer_id', on_delete=django.db.models.deletion.CASCADE, to='photoadmin.Photographer')),
            ],
            options={
                'db_table': 'photo_studio',
            },
        ),
        migrations.CreateModel(
            name='PrintingSize',
            fields=[
                ('id', models.AutoField(db_column='printing_size_id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=20)),
                ('width', models.IntegerField(db_column='width')),
                ('height', models.IntegerField(db_column='height')),
            ],
            options={
                'db_table': 'printing_size',
            },
        ),
        migrations.CreateModel(
            name='SelectionPhoto',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(db_column='selection_photo_id', primary_key=True, serialize=False)),
                ('amount', models.IntegerField(blank=True, db_column='amount', default=1, null=True)),
                ('photoshoot_photo_id', models.ForeignKey(db_column='photo_shoot_photo_id', on_delete=django.db.models.deletion.CASCADE, to='photoadmin.PhotoShootPhoto')),
                ('photoshoot_selection_id', models.ForeignKey(db_column='photo_shoot_selection_id', on_delete=django.db.models.deletion.CASCADE, to='photoadmin.PhotoShootSelection')),
                ('printing_size', models.ForeignKey(blank=True, db_column='printing_size_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='photoadmin.PrintingSize')),
            ],
            options={
                'db_table': 'selection_photo',
            },
        ),
        migrations.CreateModel(
            name='SelectionRequest',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(db_column='selection_request_id', primary_key=True, serialize=False)),
                ('client_email', models.EmailField(db_column='client_email', max_length=100)),
                ('token', models.CharField(db_column='token', max_length=100)),
                ('security_code', models.CharField(db_column='security_code', max_length=8)),
                ('received_date', models.DateTimeField(blank=True, db_column='received_date', null=True)),
                ('state', models.CharField(choices=[('PE', 'Pending'), ('OK', 'Accepted'), ('ER', 'Error')], db_column='state', default='PE', max_length=5)),
                ('error_code', models.IntegerField(blank=True, db_column='error_code', null=True)),
                ('photographer', models.ForeignKey(db_column='photographer_id', on_delete=django.db.models.deletion.CASCADE, to='photoadmin.Photographer')),
                ('photoshoot_selection_id', models.ForeignKey(db_column='photo_shoot_selection_id', on_delete=django.db.models.deletion.CASCADE, to='photoadmin.PhotoShootSelection')),
            ],
            options={
                'db_table': 'selection_request',
            },
        ),
        migrations.AddField(
            model_name='photographerphotoprinting',
            name='photoprinting',
            field=models.ForeignKey(db_column='photo_printing_id', on_delete=django.db.models.deletion.CASCADE, related_name='photographer_photoprinting', to='photoadmin.PhotoPrinting'),
        ),
    ]
