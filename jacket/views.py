from django.views import generic
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
