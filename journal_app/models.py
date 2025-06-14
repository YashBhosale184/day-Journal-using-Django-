from django.db import models

# Create your models here.


from django.db import models

class JournalEntry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Write your journal entry here.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """This is what shows up in the Django admin for each entry."""
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Journal Entries"