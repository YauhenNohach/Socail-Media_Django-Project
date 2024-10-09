from accounts.models import Post
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, UpdateView

from .forms import CustomUserCreationForm, LoginForm

# , RatingForm
from .models import CustomUser

# , Photo, Rating

# class PhotoRatingView(View):

#     def get(self, request, *args, **kwargs):
#         photo = Photo.objects.exclude(ratings__user=request.user).first()

#         if photo is None:

#             return redirect("feed")

#         form = RatingForm()
#         return render(request, "photos/rate_photo.html", {"photo": photo, "form": form})

#     def post(self, request, *args, **kwargs):
#         photo = get_object_or_404(Photo, id=request.POST.get("photo_id"))
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             rating, created = Rating.objects.update_or_create(
#                 user=request.user,
#                 photo=photo,
#                 defaults={"score": form.cleaned_data["score"]},
#             )
#             return redirect("photo_rating")
#         return render(request, "photos/rate_photo.html", {"photo": photo, "form": form})


class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = "profiles/profile_detail.html"
    context_object_name = "profile"

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs["username"])


class ProfileListView(ListView):
    model = CustomUser
    template_name = "profiles/profile_list.html"
    context_object_name = "profiles"
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = CustomUser.objects.all().order_by("username")
        if query:
            queryset = queryset.filter(Q(username__icontains=query))
        return queryset


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
