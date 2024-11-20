import os
from django.core.exceptions import ValidationError

def validate_file_size(value):
    max_size_kb = 5120  
    if value.size > max_size_kb * 1024:
        raise ValidationError(f"Fayl hajmi {max_size_kb} KB dan oshmasligi kerak.")

def validate_file_extension(value):
    valid_extensions = ['.jpg', '.jpeg', '.jfif', '.png']
    ext = os.path.splitext(value.name)[1].lower()  
    if ext not in valid_extensions:
        raise ValidationError(f"Faqat quyidagi kengaytmalar ruxsat etiladi: {', '.join(valid_extensions)}.")
