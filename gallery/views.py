from django.shortcuts import render, get_object_or_404
from .models import Image
from datetime import timedelta
from django.utils import timezone

def gallery_view(request):
    one_month_ago = timezone.now() - timedelta(days=30)
    recent_images = Image.objects.filter(created_date__gte=one_month_ago)
    return render(request, 'gallery.html', {'images': recent_images})

def image_detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    return render(request, 'image_detail.html', {'image': image})



