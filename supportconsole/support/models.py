from django.db import models

class SupportCompany(models.Model):
    name = models.CharField('Компанія', max_length=250)
    start_date = models.DateTimeField('Дата початок')
    end_date = models.DateTimeField('Дата кінець')
    status = models.BooleanField('Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "компанія"
        verbose_name_plural = "компанії"


class SupportPriority(models.Model):
    name = models.CharField('Преорітет', max_length=250)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "преорітет"
        verbose_name_plural = "преорітети"

class SupportStatus(models.Model):
    name = models.CharField('Статус', max_length=250)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "статус тікета"
        verbose_name_plural = "статус тікета"