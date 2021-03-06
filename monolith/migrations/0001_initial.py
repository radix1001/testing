# Generated by Django 3.1.2 on 2020-11-02 00:08

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('MA', 'Male'), ('FE', 'Female'), ('NF', 'Not Informed')], max_length=2)),
                ('condition', models.CharField(choices=[('AJ', 'Average Joe'), ('AT', 'Athlete')], max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
