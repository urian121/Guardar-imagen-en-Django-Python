from django.db import models


class Zapato(models.Model):
    name = models.CharField(max_length=50)
    img_zapato = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "zapatos"
        ordering = ['-created_at']
