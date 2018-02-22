from django.conf.urls import url, include
import blog
from blog import views

urlpatterns = [
    url(r'^$', blog.views.home, name='home'),
    url(r'^about/$', blog.views.about, name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', blog.views.show_article, name = 'article'),
    url(r'^contacts/$', views.EContactsView.as_view(), name='contacts'),

    url(r'^category/(?P<slug>[-\w]+)/$', blog.views.NewsList, name='news_list'),

    url(r'^information/$', blog.views.information, name='information'),

    url(r'^information/faculty/$', blog.views.faculty, name='faculty'),
    url(r'^information/schedule/$', blog.views.schedule, name='schedule'),
    url(r'^information/documentation/$', blog.views.documentation, name='documentation'),

    url(r'^library/$', blog.views.library, name='library'),
    url(r'^libraries/(?P<slug>[-\w]+)/$$', blog.views.libraries, name='libraries'),
]
