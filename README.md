# Django + Bitium JWT Authentication Backend

Installation :

* Clone this repository into your django project root
* Ensure JWT is installed


	pip install pyjwt


* Edit myproject/settings.py to include :


	BITIUM_IS_STAFF=False # Same as the django is_staff user flag
	BITIUM_IS_ACTIVE=True # Same as the django is_active user flag
	BITIUM_IS_SUPERUSER=False # Same as the manage.py createsuperuser
	BITIUM_LOGIN_URL="https://www.bitium.com/YOUR_AUTH_ENDPOINT"
	BITIUM_REDIRECT_URL="/admin" # Where to redirect your user after a successful login (optional)

	AUTHENTICATION_BACKENDS = [
		'django.contrib.auth.backends.ModelBackend', # this is the default
		'django_bitium.auth.BitiumBackend',
	]

	INSTALLED_APPS = [
		...
		'django_bitium',
	]


* Add the following to yourproject/urls.py


	from django_bitium.views import authtest, auth, deauth

	urlpatterns = [
		...
		url(r'^auth/', auth),
		url(r'^logout/', deauth),
		url(r'^authtest/', authtest),
	]


