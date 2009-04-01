======================
Application Manager
======================

This is based off a customer requirement that insists that users have the capability to turn on or off links to applications. We don't try to restrict applications themselves in Pinax at this point because that would be a major architectural change. 

This also allows us to turn on/off the links to an application, which might prove useful.

----

TODO
=======

 * convert from DL to UL
 * Template tag for displaying a user's list of applications.
 * Provide a list of approved applications that would work in Application Manager.
 * Integrate sites functionality with this application.
 * JEZDEZ suggested some middleware to control access to applications via 403 errors - http://code.djangoproject.com/browser/django/trunk/django/http/__init__.py#L419
 * Introspect to pre-populate the Admin interface with the list of all
   applications installed
 
Completed TODO
=================
 * Create way to display a few content items if desired. The generic item functions used elsewhere in Pinax serves as a nice guide.
 * Independent of Pinax. 
 * Migrate over to its own google project
 * Provide UI for allowing users to enable or disable applications
 

INSTALL
=======

Download it into the project's ``apps/`` dir like::

 svn co http://django-application-manager.googlecode.com/svn/trunk/application_manager

(TODO: try doing this with pip in the requirements file).

Edit your project's ``settings.py`` file like::

  INSTALLED_APPS = (
      # included
      'django.contrib.auth',
      ...
      # external
      'notification', # must be first
      'application_manager',
      'django_openid',
      ...

Re-sync the DB to add the new tables and restart the server::

       ./manage.py syncdb
       ./manage.py runserver

You should see it in the admin interface at::

  http://localhost:8000/admin/
  http://localhost:8000/admin/application_manager/

USAGE
=====

Admin
-----

In the 'admin' interface you can specify apps that can be
enabled/disabled. 

[TODO: I don't know what you fill in these fields here]

User Level
----------

Add the applications_manager to the urls.py::

    (r'^application_manager/', include('application_manager.urls')),

We create a section in the Pinax profile page to manage this:

* copy the stock profile app from .../pinax/apps/profiles to your
  project's apps dir .../pinax/projects/social_project/apps/profiles
* copy the stock profile templates from
  .../pinax/templates/default/profiles
  to
  .../pinax/projects/social_project/templates/profiles

(TODO: why can't I make it work by copying the stock templates into
apps/profiles/templates/profiles/ so they can be together)

Now you can modify it to include a section for the Application
Manager.  We do it in ``profile.html`` but I suppose you could do it
in the ``profile_right_panel.html``::

            {% if is_me %}
	        {% include "application_manager/applications.html" %}
                <div class="form-toggle">

Then your customized apps/profiles/view.py do the import and return
``applications`` in the response data::

  from application_manager.views import get_applications
  ...
      response_dictionary = {
	      "applications": get_applications(request),
	      "profile_form": profile_form,

If you load the profiles page you should see a lit of apps which have
been added by in the Admin interface. 

