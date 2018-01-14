from django.shortcuts import render, redirect, get_object_or_404
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
    template_name = "jacket/index.html"

    if request.method == 'POST':
        search_string = request.POST['search']
        if search_string == '':
            context = {'jackets': Jacket.objects.all().order_by('-added_on'), 'source': 'search'}
            return render(request, template_name, context)
        search_fields = ['title', 'description', 'location']
        f = search_filter(search_fields, search_string)
        context = {'jackets': Jacket.objects.filter(f).order_by('-added_on'), 'source': 'search'}
        return render(request, template_name, context)
    else:
        context = {'jackets': Jacket.objects.all().order_by('-added_on'), 'source': 'search'}
        return render(request, template_name, context)


def your_jackets(request):
    if request.user.is_authenticated:
        template_name = "jacket/index.html"
        user_jackets = Jacket.objects.filter(added_by_id=request.user.id)
        return render(request, template_name, {'jackets': user_jackets, 'source': 'your-jackets'})
    else:
        return redirect('index')


def mark_returned(request, jacket_id):
    jacket = get_object_or_404(Jacket, pk=jacket_id)
    if request.user.is_authenticated and request.user.pk == jacket.added_by_id:
        jacket.returned = False if jacket.returned is True else True
        jacket.save()
        return redirect('jacket:details', pk=jacket_id)
    else:
        return redirect('index')
