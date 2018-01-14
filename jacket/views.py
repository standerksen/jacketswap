from django.shortcuts import render
from django.views import generic
from simple_search import search_filter
from .models import Jacket
from .forms import CreateJacketForm


class JacketIndex(generic.ListView):
    template_name = 'jacket/index.html'

    jackets_list = Jacket.objects.all()

    def get_queryset(self):
        return self.jackets_list

    def get_context_data(self, **kwargs):
        context = super(JacketIndex, self).get_context_data(**kwargs)
        # Possible add to context by using context['item'] = item here
        return context


class JacketDetails(generic.DetailView):
    template_name = 'jacket/details.html'
    model = Jacket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Possible add to context by using context['item'] = item here
        return context


class JacketCreate(generic.CreateView):
    form_class = CreateJacketForm
    template_name = 'jacket/create.html'
    model = Jacket

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        form.save()
        return super().form_valid(form)


def search_results(request):
    template_name = "jacket/search.html"

    if request.method == 'POST':
        search_string = request.POST['search']
        if search_string == '':
            context = {'jackets': Jacket.objects.all()}
            return render(request, template_name, context).order_by('-added_on')
        search_fields = ['title', 'description', 'location']
        f = search_filter(search_fields, search_string)
        context = {'jackets': Jacket.objects.filter(f).order_by('-added_on')}
        return render(request, template_name, context)
    else:
        context = {'jackets': Jacket.objects.all()}
        return render(request, template_name, context).order_by('-added_on')
