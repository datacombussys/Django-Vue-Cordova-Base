# from django.db import models
# from organizations.models import Organization, OrganizationOwner, OrganizationUser
# from organizations.utils import create_organization


# class BusinessOrg(Organization):
#     mailing_address = models.CharField(max_length=50)


# class MerchantAccountUser(models.Model):
#     firstName = models.CharField(max_length=50)


# class MerchantAccountOwner(models.Model):
#     mailing_address = models.CharField(max_length=50)


'''Types of Model inheritance
Abstract Inheritance - Provides a base class and inheriting classes use its fields to generate the new classes. There is  not base class generated in the database of the Abstract model. Use the folowing syntax
    Parent model class:
    class Meta:
    abstract = true

Multi-Table Inheritance - Used when each model (parent and child) in the hierarchy needs to have its own table in the database.

Proxy Inheritance - Inherit from base class and add own properties but not fields.  Cannot add fields. Cannot Use abstract class. Can override parent models but not extend. Query would take place on the parent model.

'''