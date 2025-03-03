from django.db import models


class OriginSpecification(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class OriginModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    specifications = models.ManyToManyField(OriginSpecification)

    def __str__(self):
        return self.name


class CustomOriginSpecification(models.Model):
    character = models.ForeignKey(
        'Character', on_delete=models.CASCADE,
        related_name='origin_specification_custom'
    )
    race_background = models.ForeignKey(
        OriginSpecification, on_delete=models.CASCADE,
        related_name='origin_specification_custom',
    )
    custom_description = models.TextField(
        verbose_name="Пользовательское описание", blank=True, null=True
    )
    hide_original = models.BooleanField(
        verbose_name="Скрыть оригинальный текст", default=False
    )
