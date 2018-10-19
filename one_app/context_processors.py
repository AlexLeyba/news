from one_app.models import PodСategory
from one_app.forms import Search


def category(request):
    #category = PodСategory.objects.filter(category__name="Классы")
    pod_cat = PodСategory.objects.all()
    search = Search()
    return {"pod_cat": pod_cat, "search": search}
