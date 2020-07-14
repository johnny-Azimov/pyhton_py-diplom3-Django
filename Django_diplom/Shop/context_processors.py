from .models import Section


def sections(request):
    return {"drop_menu": Section.objects.all()}
