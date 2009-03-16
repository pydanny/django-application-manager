======================
Application Manager
======================

This is based off a customer requirement that insists that users have the capability to turn on or off links to applications. We don't try to restrict applications themselves in Pinax at this point because that would be a major architectural change. 

This also allows us to turn on/off the links to an application, which might prove useful.

----

TODO
=======

 * Migrate over to its own google project
 * Improve the model docs since that will heavily drive usability of this application.
 * Template tag for displaying a user's list of applications.
 * Provide UI for allowing users to enable or disable applications
 * Provide a list of approved applications that would work in Application Manager.
 * Integrate sites functionality with this application.
 * JEZDEZ suggested some middleware to control access to applications via 403 errors - http://code.djangoproject.com/browser/django/trunk/django/http/__init__.py#L419
 
Completed TODO
=================
 * Create way to display a few content items if desired. The generic item functions used elsewhere in Pinax serves as a nice guide.
 * Independent of Pinax. 
 