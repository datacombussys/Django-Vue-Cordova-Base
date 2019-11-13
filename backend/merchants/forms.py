# from django import forms
# from django.conf import settings
# from django.contrib.sites.models import Site
# from organizations.backends import invitation_backend
# from organizations.backends.forms import UserRegistrationForm

# from organizations.forms import OrganizationForm, OrganizationUserAddForm, OrganizationUserForm, OrganizationAddForm, SignUpForm
# from .models import MerchantAccount, MerchantAccountUser, MerchantAccountOwner


# class OrgForm(OrganizationForm):
#     """Form class for updating Organizations"""
#     class Meta:
#         model = MerchantAccount
#         exclude = []


# class UserForm(forms.ModelForm):
#     """Form class for updating OrganizationUsers"""
#     """
#     Form class for editing OrganizationUsers *and* the linked user model.
#     """
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField()

#     class Meta:
#         exclude = ('user', 'is_admin')
#         model = MerchantAccountUser

#     def __init__(self, *args, **kwargs):
#         super(AccountUserForm, self).__init__(*args, **kwargs)
#         if self.instance.pk is not None:
#             self.fields['first_name'].initial = self.instance.user.first_name
#             self.fields['last_name'].initial = self.instance.user.last_name
#             self.fields['email'].initial = self.instance.user.email

#     def save(self, *args, **kwargs):
#         """
#         This method saves changes to the linked user model.
#         """
#         if self.instance.pk is None:
#             site = Site.objects.get(pk=settings.SITE_ID)
#             self.instance.user = invitation_backend().invite_by_email(
#                 self.cleaned_data['email'], **{
#                     'first_name': self.cleaned_data['first_name'],
#                     'last_name': self.cleaned_data['last_name'],
#                     'organization': self.cleaned_data['organization'],
#                     'domain': site
#                 })
#         self.instance.user.first_name = self.cleaned_data['first_name']
#         self.instance.user.last_name = self.cleaned_data['last_name']
#         self.instance.user.email = self.cleaned_data['email']
#         self.instance.user.save()
#         return super(AccountUserForm, self).save(*args, **kwargs)


# class newOrgForm(OrganizationAddForm):
#     """
#     Generates a registration ModelForm for the given organization model class
#     """
#     pass


# class newUserForm(OrganizationUserAddForm):
#     pass


# class RegistrationForm(UserRegistrationForm):
#     """
#     Form class that allows a user to register after clicking through an
#     invitation.
#     """
#     pass