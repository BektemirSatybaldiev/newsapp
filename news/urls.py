from django.contrib.auth.views import LogoutView
from django.urls import path
from newsapp import settings
from .views import MainView, PostDetailView, SignUpView, SignInView, SuccessView, FeedBackView, SearchView, TagView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('news/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('search/', SearchView.as_view(), name='search'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout'),
    path('contact/success/', SuccessView.as_view(), name='success'),
    path('tag/<slug:slug>/', TagView.as_view(), name="tag"),
]

