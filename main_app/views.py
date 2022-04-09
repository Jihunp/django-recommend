from django.forms import ValidationError
from django.urls import reverse
from dataclasses import fields
from pipes import Template
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Act, Review
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
# auth imports
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CustomUserCreationForm



class Home(View):    
    def get(self, request):
        return HttpResponse("Wholesome Home")

class About(View):
    def get(self, request):
        return HttpResponse("About Wholesome")

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"


class ActList(TemplateView):
    template_name = 'actlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["acts"] = Act.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["acts"] = Act.objects.all()
            context["header"] = "Activities"
        return context

@method_decorator(login_required, name='dispatch')
class ActCreate(CreateView):
    model = Act
    fields = '__all__'
    # fields = ['name', 'label', 'rating', 'price', 'location', 'images', 'review']
    template_name = 'act_create.html'
    def get_success_url(self):
        return reverse('act_detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/activities')

class ActDetail(DetailView):
    model = Act
    template_name = "act_detail.html"

@method_decorator(login_required, name='dispatch')
class ActUpdate(UpdateView):
    model = Act
    # fields = ['name', 'label', 'rating', 'price', 'location', 'images', 'review']
    fields = '__all__'
    template_name = "act_update.html"
    def get_success_url(self):
        return reverse('act_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class ActDelete(DeleteView):
    model = Act
    template_name = "act_delete_confirm.html"
    success_url = "/activities"

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    acts = Act.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'acts': acts})

# Reviews Crud
def reviews_index(request):
    reviews = Review.objects.all()
    return render(request, 'reviews_index.html', {'reviews': reviews})

def reviews_show(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'reviews_show.html', {'review': review})

@method_decorator(login_required, name='dispatch')
class ReviewCreate(CreateView):
    model = Review
    fields = '__all__'
    template_name ='review_form.html'
    success_url = '/reviews'

@method_decorator(login_required, name='dispatch')
class ReviewUpdate(UpdateView):
    model = Review
    fields = ['name', 'description', 'weather', 'active']
    template_name = 'reviews_update.html'
    success_url = '/reviews'

@method_decorator(login_required, name='dispatch')
class ReviewDelete(DeleteView):
    model = Review
    template_name = 'review_confirm_delete.html'
    success_url = '/reviews'

# django auth
# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             print('Hello', user.username)
#             messages.success(request, 'Account Created Successfully')
#             return HttpResponseRedirect('/user/'+str(user))
#         else:
#             return render(request, 'signup.html', {'form': form})
#     else:
#         form = UserCreationForm()
#         return render(request, 'signup.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save_login()
            login(request, user)
            messages.success(request, 'Account Created')
            return HttpResponseRedirect('/user/'+str(user))
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/activities')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usr = form.cleaned_data['username']
            pas = form.cleaned_data['password']
            user = authenticate(username = usr, password = pas)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+usr)
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request,'register.html', {'form': form}) 
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    