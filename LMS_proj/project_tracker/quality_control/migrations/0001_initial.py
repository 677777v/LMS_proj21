# Generated by Django 5.0.4 on 2024-04-20 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('New', 'Новая'), ('In_progress', 'В работе'), ('Completed', 'Завершена')], default='New', max_length=50)),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'Low'), (2, 'Medium-Low'), (3, 'Medium'), (4, 'Medium-High'), (5, 'High')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bug_reports', to='tasks.project')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bug_reports', to='tasks.task')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Under_consideration', 'Рассмотрение'), ('Accepted', 'Принято'), ('Rejected', 'Отклонено')], default='Under_consideration', max_length=50)),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'Low'), (2, 'Medium-Low'), (3, 'Medium'), (4, 'Medium-High'), (5, 'High')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_requests', to='tasks.project')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feature_requests', to='tasks.task')),
            ],
        ),
    ]
