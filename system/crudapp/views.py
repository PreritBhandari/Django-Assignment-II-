from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from .forms import ProfileUpdateForm, UserUpdateForm
from .models import Blog, Profile


class crud_home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'crudapp/crudhome.html')
        return redirect('login')


class PostListView(ListView):
    model = Blog
    template_name = 'crudapp/bloglist.html'
    context_object_name = 'posts'
    ordering = ['date']


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'crudapp/blogcreate.html'
    success_url = '/crudapp/blog/'
    fields = ['title', 'content']

    # author set garna lai yo talako
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'content']
    template_name = 'crudapp/update.html'
    success_url = '/crudapp/blog'

    # author set garna lai yo talako
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/crudapp/blog/'
    template_name = 'crudapp/delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def blog_view(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'users/rate.html', context)


class profile(View):
    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        #
        # instance = ko le form bhitra data haru dinxa kholda kheri taki ramrari update garna paos .
        # tyo lekhena bhane khali hunxa tyo field tessai.

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated.')
            return redirect('profile')
        context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return render(request, 'crudapp/profile.html', context)

    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)

        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return render(request, 'crudapp/profile.html', context)


class ProfileCreate(CreateView):
    model = Profile
    template_name = 'crudapp/profilecreate.html'
    success_url = '/crudapp/profile'
    fields = ['image', 'user']
