from django.db import models
from tasks.models import Project, Task

class BugReport(models.Model):
    STATUS_CHOISES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium-Low'),
        (3, 'Medium'),
        (4, 'Medium-High'),
        (5, 'High')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='bug_reports',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='bug_reports',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOISES,
        default='New'
    )
    priority = models.PositiveSmallIntegerField(
        choices=PRIORITY_CHOICES,
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FeatureRequest(models.Model):
    STATUS_CHOISES = [
        ('Under_consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium-Low'),
        (3, 'Medium'),
        (4, 'Medium-High'),
        (5, 'High')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='feature_requests',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='feature_requests',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOISES,
        default='Under_consideration'
    )
    priority = models.PositiveSmallIntegerField(
        choices=PRIORITY_CHOICES,
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
