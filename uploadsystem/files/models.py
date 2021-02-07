from django.db import models
import uuid
import os
from PIL import Image
from datetime import datetime
from django.utils import timezone


def userimage_profile_file_path(instance, file_name):
    """Generate File path for new user image"""
    ext = file_name.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join("uploads/user/profile", filename)

class Files(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    created = models.DateField(auto_created=True)
    updated = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(default= "default.jpeg",upload_to=userimage_profile_file_path,blank=True, null = True)
    
    def __str__(self):
        return f"{self.id} File"

    def save(self):
        super().save()
        img = Image.open(self.file.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.file.path)






