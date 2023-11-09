# Generated by Django 4.2.7 on 2023-11-09 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocioUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=200, null=True, verbose_name='Full Name')),
                ('phone_number', models.CharField(max_length=11, null=True, unique=True, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='Email')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='socio', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Socio Profile',
            },
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('facebook_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Facebook Account')),
                ('twitter_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Twitter Account')),
                ('pinterest_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Pinterest Account')),
                ('tumbler_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Tumbler Acount')),
                ('github_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Github Account')),
                ('linkedin_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='LinkedIn Account')),
                ('instagram_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Instagram Account')),
                ('discord_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Discord Account')),
                ('tiktok_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Tiktok Account')),
                ('thread_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Thread Account')),
                ('gravater_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Gravater Account')),
                ('youtube_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Youtube Account')),
                ('whatsapp_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='WhatsApp Account')),
                ('redit_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Redit Account')),
                ('skype_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Skype Account')),
                ('telegram_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Telegram Account')),
                ('spotify_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Spotify Account')),
                ('behance_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Behance Account')),
                ('soundcloud_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='SoundCloud Account')),
                ('socio_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social_link', to='socio_profile.sociouser', verbose_name='Socio User')),
            ],
            options={
                'verbose_name_plural': 'Socio User Social Media Links',
            },
        ),
        migrations.AddIndex(
            model_name='sociouser',
            index=models.Index(fields=['id', 'user', 'phone_number', 'email'], name='socio_profi_id_f3c8a9_idx'),
        ),
        migrations.AddIndex(
            model_name='sociallinks',
            index=models.Index(fields=['id', 'socio_user'], name='socio_profi_id_881165_idx'),
        ),
    ]
