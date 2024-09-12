# Sylvie

This an API to get the data from PLC to monitor its status

## Current apps

### WIP (Nothing here for now...)

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/UMRGRS/Sylvie.git
    $ cd Sylvie
    
Create and activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
Then simply apply the migrations:

    $ python manage.py migrate

You can now run the development server:

    $ python manage.py runserver
