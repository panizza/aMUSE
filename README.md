aMUSEment for the masses
=====
---------------------
###SOLO LA PRIMA VOLTA

*  installare python-pip (per python2)
*  da pip installare virtualenvwrapper
*   `echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc`
*   echo 'source' `which virtualenvwrapper.sh` >> ~/.bashrc
*   `mkvirtualenv --no-site-packages amuse`
*  `workon amuse`
*  clonare il repository e posizionarsi dentro (cd aMUSE)
*  `git checkout devel`
*  `pip install -r requirements/essentials.txt` (NON da superuser)
*  `python manage.py syncdb`
*  `python manage.py migrate`

###OGNI VOLTA CHE SI VUOLE LAVORARE

* `workon amuse`
avviare il server con *   `python manage.py runserver`
