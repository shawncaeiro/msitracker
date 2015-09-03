# msitracker
*Prototyped Sales Tracking and Analytics Solution*
## Demo
[Visit Site](https://www.msitimetracker.herokuapp.com)

Hosted on a `free` Heroku dyno. This may lead to delays* when loading the initial page or site downtime**. 

*Dyno will sleep after 30 minutes of inactivity. If during this sleep a person enters the site, the dyno will restart, a process taking ~20 seconds. After initial delay, the site will function normally.

**Dyno will also sleep for 6 hours after 18 hours of use per 24 hours; attempting to access the site during this time will result in an error.

## Hosting Locally

### Prerequisites

Please ensure the following are installed in your environment:

* [Python 2.7.x](https://www.python.org/downloads/)
* [Pip](https://pip.pypa.io/en/latest/installing.html)
* [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

### Steps

1. Clone or download repository into your local directory.
2. Create and activate virtualenv for that directory. In your command line enter the following commands:

```
$ virtualenv venv
$ source venv/bin/activate
```
3. Install the necessary packages with the command:
```
$ pip install -r requirements.txt
```
4. In the file msitracker/settings.py, change the value of DATABASES['default'] to your local database settings.
    * [Settings Documentation](https://docs.djangoproject.com/en/1.8/ref/settings/)
5. In command line run:
```
$ python manage.py runserver
```
6. View site at [http://127.0.0.1:8000](http://127.0.0.1:8000)

