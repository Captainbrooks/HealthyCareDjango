# Generated by Django 5.1.7 on 2025-04-21 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_doctors_is_extraordinary'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeslots', to='doctors.doctors')),
            ],
            options={
                'unique_together': {('doctor', 'appointment_date', 'appointment_time')},
            },
        ),
        migrations.AddField(
            model_name='doctors',
            name='available_timeslots',
            field=models.ManyToManyField(blank=True, null=True, to='doctors.timeslot'),
        ),
    ]
