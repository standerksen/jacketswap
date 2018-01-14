from django.shortcuts import redirect, render
from django.views.generic import View
from jacket.models import Jacket


class IndexView(View):

    def get(self, request):
        jackets_list = Jacket.objects.all().order_by('-added_on')[:10]
        return render(request, 'generic/index.html', {'jackets': jackets_list})
