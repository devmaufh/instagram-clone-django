from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from platzigram import views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('hello-world/', views.hello_world),
                  path('hi/', views.hi),
                  path('posts/', posts_views.list_posts, name='feed'),
                  path('users/login/', users_views.login_view, name='login'),
                  path('users/logout/', users_views.logout_view, name='logout'),
                  path('users/signup', users_views.sign_up, name='signup'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
