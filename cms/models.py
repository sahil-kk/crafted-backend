from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    college = models.CharField(max_length=150)
    image_url = models.URLField(blank=True)

    class Meta:
            verbose_name_plural = "Faculties"
    def __str__(self):
        return self.name