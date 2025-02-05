from django.db import models


class LineamentModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class CustomLineament(models.Model
                      ):
    character = models.ForeignKey(
        'Character', on_delete=models.CASCADE,
        related_name='lineament_custom'
    )
    lineament = models.ForeignKey(
        LineamentModel, on_delete=models.CASCADE,
        related_name='lineament_custom',
    )
    custom_description = models.TextField(
        verbose_name="Пользовательское описание", blank=True, null=True
    )
    hide_original = models.BooleanField(
        verbose_name="Скрыть оригинальный текст", default=False
    )
