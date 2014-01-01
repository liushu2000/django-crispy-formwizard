from django.shortcuts import render_to_response, render, redirect
from django.contrib.formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from forms import ContactForm
from django import forms
from models import Contact
from forms import ContactForm2
import collections
import datetime

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

        return redirect('/contacts/')
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


        return redirect('/contacts_crispy/')
        # return render_to_response('done.html', {
        #     'form_data': [form.cleaned_data for form in form_list],
        # })
    # def contact(request):
    #     if request.method == 'POST': # If the form has been submitted...
    #         form = ContactForm(request.POST) # A form bound to the POST data
    #         if form.is_valid(): # All validation rules pass
    #             # Process the data in form.cleaned_data
    #             # ...
    #             return HttpResponseRedirect('/thanks/') # Redirect after POST
    #     else:
    #         form = ContactForm() # An unbound form
    #
    #     return render(request, 'contact_form.html', {
    #         'form': form,
    #     })