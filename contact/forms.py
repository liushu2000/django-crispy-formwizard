__author__ = 'shu'

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class ContactForm1(forms.Form):

    name = forms.CharField(max_length=20, help_text='Maximum 20 chars.')
    email = forms.EmailField()

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
    Field('name', css_class='input-xlarge'),
    Field('email', rows="3", css_class='input-xlarge'),
    # 'radio_buttons',
    # Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
    # AppendedText('appended_text', '.00'),
    # PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
    # PrependedText('prepended_text_two', '@'),
    # 'multicolon_select',
    FormActions(
        Submit('save_changes', 'Next', css_class="btn-primary"),
        Button('cancel', 'Cancel', onclick='window.location.href="{}"'.format('/contacts_crispy/')),
                )
    )

class ContactForm2(forms.Form):
    memo = forms.CharField(widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm2'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Next'))
        super(ContactForm2, self).__init__(*args, **kwargs)

class ContactForm3(forms.Form):
    phone = forms.CharField()

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
    Field('phone', css_class='input-xlarge'),
    Field('location', rows="3", css_class='input-xlarge'),
    # 'radio_buttons',
    # Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
    # AppendedText('appended_text', '.00'),
    # PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
    # PrependedText('prepended_text_two', '@'),
    # 'multicolon_select',
    FormActions(
        Submit('save_changes', 'Save', css_class="btn-primary"),
        Button('cancel', 'Cancel', onclick='window.location.href="{}"'.format('/contacts_crispy/')),
        # Button('cancel', 'Cancel', onclick='history.go(-1);'),
                )
    )

class ContactForm(forms.Form):
    Name = forms.CharField(max_length=20, help_text='Maximum 20 chars.')
    Email = forms.CharField()
    Memo = forms.EmailField()
    Terms = forms.BooleanField(required=False)