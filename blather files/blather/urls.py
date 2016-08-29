from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from blat import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'blather.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name="homepage"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout, name="logout"),
    url(r'^my/$', views.MyView.as_view(), name="myview"),
    url(r'^create/$', views.NewBlatView.as_view(), name="newblat"),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.EditBlatView.as_view(), name="editblat"),
]
