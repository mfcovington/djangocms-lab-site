from django.conf import settings

def lab_settings(request):
    return {
        'LAB_NAME': settings.LAB_NAME,
    }
