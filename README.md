aMUSEment for the masses
=====
---------------------
###SOLO LA PRIMA VOLTA

1.  installare python-pip (per python2)

2.  da pip installare virtualenvwrapper
*   `echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc`
*   `echo "source" `which virtualenvwrapper.sh` >> ~/.bashrc`

3.  `mkvirtualenv --no-site-packages amuse`

4.  `workon amuse`

5.  clonare il repository e posizionarsi dentro (cd aMUSE)

6.  `git checkout devel`

7.  `pip install -r requirements/essentials.txt` (NON da superuser)

8.  `python manage.py syncdb`

9.  `python manage.py migrate`


###OGNI VOLTA CHE SI VUOLE LAVORARE

1. `workon amuse`

2. per avviarei il server
*   `python manage.py runserver`
