from django import forms
from django.contrib import admin
from models import FlatPage
from django.utils.translation import ugettext_lazy as _


class FlatpageForm(forms.ModelForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/\.~]+$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                          " dots, underscores, dashes, slashes or tildes."))

    class Meta:
        model = FlatPage

    class Media:
        js = [
            '/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/admin/tinymce_setup/tinymce_setup.js',
        ]


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', )}),
    )
    list_display = ('url', 'title')
    search_fields = ('url', 'title', 'content', )

admin.site.register(FlatPage, FlatPageAdmin)
