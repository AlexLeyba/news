from one_app.models import Category
from one_app.forms import Search


def category(request):
    category = Category.objects.all()
    search = Search()
    return {"categories": category, "search": search}
