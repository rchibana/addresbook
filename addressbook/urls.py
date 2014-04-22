from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import contacts.views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    url(r'^list$', contacts.views.ListContactView.as_view(),
        name='contact.list',),
    url(r'^new$', contacts.views.CreateContactView.as_view(),
        name='contact.new',),
    url(r'^edit/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(),
        name="contact.edit",),
    url(r'^delete/(?P<pk>\d+)/$', contacts.views.DeleteContactView.as_view(),
        name="contact.delete",),
    url(r'^view/(?P<pk>\d+)/$', contacts.views.ContactView.as_view(),
        name="contact.view",),
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^addressbook/', include('addressbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
