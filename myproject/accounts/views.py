from django.views.generic import ListView

from accounts.models import Post


class FeedView(ListView):
    model = Post
    template_name = "feed.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all().order_by("-created_at")
