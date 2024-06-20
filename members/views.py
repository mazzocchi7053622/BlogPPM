from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ProfilePageForm
from elaboratoPPM.models import Profile, Category


class CreateProfilePAgeView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CreateProfilePAgeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'età', 'città','hobby','website_url', 'facebook_url', 'instagram_url']
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(EditProfilePageView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'


    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name ='registration/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UserRegisterView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name ='registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UserEditView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
