from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from contact.forms import ContactForm1, ContactForm2,ContactForm3
from contact.views import ContactWizard, ContactWizard_crispy

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'formwizard.views.home', name='home'),
    # url(r'^formwizard/', include('formwizard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # (r'^contact/$', 'contact.views.contact'),
    (r'^contacts/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),
    (r'^contacts_crispy/$', ContactWizard_crispy.as_view([ContactForm1, ContactForm2, ContactForm3])),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
