# Generated by Django 5.0 on 2023-12-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=255)),
                ('date_report', models.CharField(max_length=255)),
                ('device', models.CharField(max_length=255)),
                ('cable', models.CharField(max_length=20)),
                ('power', models.CharField(max_length=255)),
                ('report', models.CharField(max_length=20000)),
                ('other_job', models.CharField(max_length=20000)),
                ('exist', models.CharField(max_length=20000)),
                ('propose', models.CharField(max_length=20000)),
                ('date', models.CharField(max_length=255)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(default='default username', max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('avatar', models.CharField(max_length=1000)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
