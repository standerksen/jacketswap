from django.shortcuts import redirect, render
from django.views.generic import View


class IndexView(View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return redirect('')

        return render(request, 'generic/index.html', {})
