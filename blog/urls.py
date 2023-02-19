from django.urls.conf import path
from .views import blog, blog_detail, blog_like

app_name = 'blog'
urlpatterns = [
    path('', blog, name='blogs'),
    path('<slug>/', blog_detail, name='post-detail'),
    path('like/<slug>/', blog_like, name='like-post')
]
