from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from contact.forms import ContactForm1, ContactForm2,ContactForm3
from contact.views import ContactWizard, ContactWizard_crispy,XEditableColumnsDatatableView,\
    user_list,User_display, user_test, UserListJson,users_plain,users_bitbucket, set_language

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'formwizard.views.home', name='home'),
    # url(r'^formwizard/', include('formwizard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # (r'^contact/$', 'contact.views.contact'),
    (r'^contacts/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),
    (r'^create_user/$', ContactWizard_crispy.as_view([ContactForm1, ContactForm2, ContactForm3])),
    (r'^users/$', XEditableColumnsDatatableView.as_view()),
    (r'^users_list/$', user_list),
    (r'^users_display/$', User_display.as_view()),
    (r'^user_test/$', user_test),

    url(r'^user_list_json/', UserListJson.as_view(), name="user_list_json"),
    (r'^users_bitbucket/$', users_bitbucket,),
    (r'^users_plain/$', users_plain,),

    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^setlang/$', set_language),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
