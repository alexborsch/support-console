from django.db import models
from django.conf import settings
from support import models as support
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField


class SupportTikets(models.Model):
    issue = models.CharField('Причина звернення', max_length=250)
    department = models.ForeignKey(support.SupportCompany, on_delete=models.SET_NULL, null=True, verbose_name='Контрагент')
    priority = models.ForeignKey(support.SupportPriority, on_delete=models.SET_NULL, null=True, verbose_name='Преорітет')
    message = models.TextField('Повідомлення')
    img = models.ImageField('Скріншот', upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField('Дата', auto_now_add=True)
    created_by = CurrentUserField()
    status = models.ForeignKey(support.SupportStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.issue

    class Meta:
        verbose_name = "тікет"
        verbose_name_plural = "тікет"

class SupportDevelopment(models.Model):
    issue = models.CharField('Назва', max_length=250)
    department = models.ForeignKey(support.SupportCompany, on_delete=models.SET_NULL, null=True, verbose_name='Контрагент')
    priority = models.ForeignKey(support.SupportPriority, on_delete=models.SET_NULL, null=True, verbose_name='Преорітет')
    message = models.TextField('Опис розробки')
    created_at = models.DateTimeField('Дата', auto_now_add=True)
    created_by = CurrentUserField()
    status = models.ForeignKey(support.SupportStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id) + " | " + str(self.created_at)

    class Meta:
        verbose_name = "заявку на розробку"
        verbose_name_plural = "заявка на розробку"