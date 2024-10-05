from accounts.models import Post
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView

from .forms import CustomUserCreationForm, LoginForm


class FeedView(ListView):
    model = Post
    template_name = "feed.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all().order_by("-created_at")


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "registration/register.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            print("User saved:", user)
            login(request, user)
            return redirect("feed")
        else:
            print("Form errors:", form.errors)
        return render(request, "registration/register.html", {"form": form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("feed")
            else:
                form.add_error(None, "password incorrect.")
        return render(request, "login/login.html", {"form": form})
