# Generated by Django 4.0 on 2022-03-26 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(blank=True, max_length=120)),
                ('phone_number', models.IntegerField(blank=True)),
                ('country', models.CharField(max_length=120)),
                ('province_state', models.CharField(max_length=250)),
                ('postal_zip', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]