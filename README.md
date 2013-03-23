aMUSEment for the masses
=====
INFO PER INSTALLAZIONE E UTILIZZO
---------------------
###SOLO LA PRIMA VOLTA

*  installare python-pip (per python2)
*  da pip installare virtualenvwrapper (http://lilihan.cn/painless-way-to-setup-virtualenv-and-virtualenvwrapper-on-ubuntu-10-10/)

*  `mkvirtualenv --no-site-packages amuse`
*  `workon amuse`
*   clonare il repository e posizionarsi dentro (cd aMUSE)
*  `git checkout devel`
*  `pip install -r requirements/essentials.txt` (NON da superuser)
*  `python manage.py syncdb`
*  `python manage.py migrate`
*  `python manage.py createsuperuser`

###OGNI VOLTA CHE SI VUOLE LAVORARE

* `workon amuse`
* avviare il server con `python manage.py runserver`


API REFERENCE
---------------------
###GET
* api/e/ -> return a list of all the exhibitions
* api/e/`id_exhibition`/ -> return the info about one exhibition
* api/e/`id_exhibition`/i/ -> return the items referred to an exhibition
* api/i/`id_item`/ -> return the info about one item

###POST
* api/exp/s/ -> allow the devices to save an experience
