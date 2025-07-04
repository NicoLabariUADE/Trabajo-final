from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Page
from .forms import PageForm
from django.db.models import Q


def pages_list(request):
    query = request.GET.get('q')
    if query:
        pages = Page.objects.filter(
            Q(title__icontains=query) |
            Q(subtitle__icontains=query) |
            Q(content__icontains=query)
        )
    else:
        pages = Page.objects.all()
    return render(request, 'pages/pages_list.html', {'pages': pages})

def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'pages/page_detail.html', {'page': page})

def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pages_list')
    else:
        form = PageForm()
    return render(request, 'pages/page_form.html', {'form': form})

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages_list')

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages_list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages_list')

class PageListView(ListView):
    model = Page
    template_name = 'pages/pages_list.html'
    context_object_name = 'pages'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Page.objects.filter(
                Q(title__icontains=query) |
                Q(subtitle__icontains=query) |
                Q(content__icontains=query)
            )
        return Page.objects.all()

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'