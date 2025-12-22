from django.db import models
from django.contrib.auth.models import User

class VaultItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    encrypted_data = models.TextField()
    uploaded_file = models.FileField(upload_to='vault_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
