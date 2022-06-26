from django.shortcuts import render
from django.db.models import Q
from app_user.models import Avatar

# Create your views here.
def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}