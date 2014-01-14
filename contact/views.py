from django.shortcuts import redirect, render_to_response, render
from django.contrib.formtools.wizard.views import SessionWizardView
from django import forms, http
from models import Contact
from forms import ContactForm2
import collections
from datatableview.views import XEditableDatatableView, DatatableView
from datatableview import helpers
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from formwizard import settings
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import translation
from django.utils.translation import check_for_language


def set_language(request):

    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    response = http.HttpResponseRedirect(next)
    if request.method == 'GET':
        lang_code = request.GET.get('language', None)
        if lang_code and check_for_language(lang_code):
            if hasattr(request, 'session'):
                request.session['django_language'] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
            translation.activate(lang_code)
    return response


@csrf_exempt
def users_plain(request):

    #users = Contact.objects.all()
    if request.method == 'GET':
        users = Contact.objects.all()
        paginator = Paginator(users, 1) # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            users = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            users = paginator.page(paginator.num_pages)

    else:
        query = request.POST.get('q')
        if query:
            users = Contact.objects.filter(name=query)

    return render_to_response('user_grid4.html', {"users": users,},)

    #return render_to_response('user_grid4.html', {'users': users})


def users_bitbucket(request):

    #from autofixture import AutoFixture
    #fixture = AutoFixture(Contact)
    #fixture.create(120)

    #language= _("Chinese")

    context = RequestContext(request)
    if request.method == 'GET':
        language_code = request.LANGUAGE_CODE

    #translation.activate(language)



    # if settings.LANGUAGE_CODE:
    #     translation.activate(settings.LANGUAGE_CODE)
    return render_to_response('user_grid_bitbucket.html',
                              {"language_code": language_code},
                              context_instance=RequestContext(request))


class UserListJson(BaseDatatableView):
        # The model we're going to show
        model = Contact

        # define the columns that will be returned
        columns = ['name', 'email', 'phone', ]

        # define column names that will be used in sorting
        # order is important and should be same as order of columns
        # displayed by datatables. For non sortable columns use empty
        # value like ''
        order_columns = [ 'name', 'email', 'phone']

        # set max limit of records returned, this is used to protect our site if someone tries to attack our site
        # and make it return huge amount of data
        max_display_length = 500

        def render_column(self, row, column):
            # We want to render user as a custom column
            if column == 'name':
                return '%s %s' % (row.name, row.email)
            else:
                return super(UserListJson, self).render_column(row, column)

        def filter_queryset(self, qs):
            # use request parameters to filter queryset

            # simple example:
            sSearch = self.request.GET.get('sSearch', None)

            if sSearch:
                qs = qs.filter(name__istartswith=sSearch)

            # more advanced example
            filter_customer = self.request.POST.get('customer', None)

            if filter_customer:
                customer_parts = filter_customer.split(' ')
                qs_params = None
                for part in customer_parts:
                    q = Q(customer_firstname__istartswith=part)|Q(customer_lastname__istartswith=part)
                    qs_params = qs_params | q if qs_params else q
                qs = qs.filter(qs_params)
            return qs


class XEditableColumnsDatatableView(XEditableDatatableView):

    def get_queryset(self):
            return Contact.objects.filter(name='Sean')

    def get_template_names(self):
        """ Try the view's snake_case name, or else use default simple template. """
        # name = self.__class__.__name__.replace("DatatableView", "")
        # name = re.sub(r'([a-z]|[A-Z]+)(?=[A-Z])', r'\1_', name)
        return ["user_grid.html", "example_base.html"]
    #model = Contact

    datatable_options = {
        'columns': [    
            'id',
            ("Name", 'name', helpers.make_xeditable),
            ("Email", 'email', helpers.make_xeditable),
            ("Phone", 'phone', helpers.make_xeditable),
        ]
    }
class User_display(XEditableDatatableView):
    #model = Contact
    def get_queryset(self):
        return Contact.objects.filter(name='Sean')

    def get_template_names(self):
        """ Try the view's snake_case name, or else use default simple template. """
        # name = self.__class__.__name__.replace("DatatableView", "")
        # name = re.sub(r'([a-z]|[A-Z]+)(?=[A-Z])', r'\1_', name)
        return ["user_grid3.html", "example_base.html"]
    #model = Contact

    datatable_options = {
        'columns': [
            'id',
            ("Name", 'name', ),
            ("Email", 'email', ),
            ("Phone", 'phone',helpers.make_xeditable(placeholder="Enter a valid date")),
            ("Edit",)
        ]
    }
    def get_column_Edit_data(self, instance, *args, **kwargs):
    # Simplest use, "text" will be the unicode of instance.blog
        #return helpers.link_to_model(instance)

    # Specify a custom text
        return helpers.link_to_model(instance, text="Edit")


from django.shortcuts import render
import django_tables2 as tables

class User_Table(tables.Table):
    selection = tables.CheckBoxColumn()


    class Meta:
        model = Contact

def user_list(request):
    table = User_Table(Contact.objects.all())

    return render(request, 'user_grid2.html', {'table': table})


def user_test(request):
    users = Contact.objects.filter(name="Sean")
    print users
    users2 =  users.filter(email="sean@msn.com")

    return render_to_response('user_grid.html', {
            'users2': users2,
             })


class ContactWizard(SessionWizardView):

    template_name = 'contact_wizard_form.html'

    def process_step(self, form):
        current_step = self.steps.current
        if current_step == '0' and self.request.POST['0-name'] == 'Sean':

            if '1' in self.form_list:
                del self.form_list['1']

                location = forms.CharField(required=False)
                self.form_list['2'].base_fields['location'] = location
        return self.get_form_step_data(form)

    def done(self, form_list, **kwargs):

        new = Contact()
        #new.user = self.request.user
        for form in form_list:
            for k, v in form.cleaned_data.iteritems():
                setattr(new, k, v)
        new.save()

        return redirect('/users/')
        # return render_to_response('done.html', {
        #     'form_data': [form.cleaned_data for form in form_list],
        # })


class ContactWizard_crispy(SessionWizardView):

    template_name = 'contact_wizard_form_crispy.html'

    def process_step(self, form):
        current_step = self.steps.current
        if current_step == '0' and self.request.POST['0-name'] == 'Sean':
            if '1' in self.form_list:
                del self.form_list['1']
                location = forms.CharField(required=False)
                self.form_list['2'].base_fields['location'] = location

        elif current_step == '0' and self.request.POST['0-name'] != 'Sean':
            if '1' not in self.form_list:
                self.form_list[u'1'] = ContactForm2

                self.form_list = collections.OrderedDict(sorted(self.form_list.items()))

                if 'location' in self.form_list['2'].base_fields:
                    del self.form_list['2'].base_fields['location']

        return self.get_form_step_data(form)

    def done(self, form_list, **kwargs):

        new = Contact()
        #new.user = self.request.user
        for form in form_list:
            for k, v in form.cleaned_data.iteritems():
                setattr(new, k, v)
        #new['at'] = datetime.datetime.now()
        new.save()


        return redirect('/users/')
        # return render_to_response('done.html', {
        #     'form_data': [form.cleaned_data for form in form_list],
        # })
