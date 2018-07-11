# Making Blog and Templates
## We are using django framework to make a blog and templates using Bootstrap.

**First step is to start a new Django project.**

# Creating Django project
*We are using the django-admin mikku command in cmd prompt.*

**django-admin.py .** It is a script that will create the directories and files for you. You should now have a directory structure which looks like this:

```
mikku
├───manage.py
└───mikku
        settings.py
        urls.py
        wsgi.py
        __init__.py
```
**manage.py** *is a script that helps with management of the site.*

*The **settings.py** file contains the configuration of your website.*

**urls.py** *file contains a list of patterns used by urlresolver.*

# Changing settings
if u want to change the time or change the language then go for this file **mikku/setting.py**

- TIME_ZONE = '---'
- LANGUAGE_CODE = '--'

We'll also need to add a path for static files. Go down to the end of the file, and just underneath the **STATIC_URL** entry, add a new one called **STATIC_ROOT:**

* STATIC_URL = '/static/'
* STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Create a datbase for your blog
To run this command to your console **python manage.py migrate**

# Starting the web server
To run this command to your console **python manage.py runserver**.

Now all you need to do is check that your website is running. Open your browser (Firefox, Chrome, Safari, Internet Explorer or whatever you use) and enter this address:

**http://127.0.0.1:8000**

**Congratulations! You've just created your first website and run it using a web server! Isn't that awesome?**

# To add this command Ctrl+C to stop the server.
*While the web server is running, you won't see a new command-line prompt to enter additional commands. The terminal will accept new text but will not execute new commands. This is because the web server continuously runs in order to listen for incoming requests.*

To type additional commands while the web server is running, open a new terminal window and activate your virtualenv. To stop the web server, switch back to the window in which it's running and press **CTRL+C** - Control and C keys together (on Windows, you might have to press Ctrl+Break).

# Create a model
To store all the posts in our blog. And we use this model to create objects.

we can create a Django model for our blog post.

so we will create a seprate application insode our project. use this command on your console **python manage.py startapp blog**.

*You will notice that a new blog directory is created and it contains a number of files now. The directories and files in our project should look like this:*

```
mikku
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── mikku
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```    
*After creating an application, we also need to tell Django that it should use it. We do that in the file **mikku/settings.py** . We need to find **INSTALLED_APPS** and add a line containing 'blog'*

**mikku/settings.py**
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```
# Creating a blog post model

In the **blog/models.py** file we define all objects called Models – this is a place in which we will define our blog post.

Let's open **blog/models.py**, remove everything from it, and write code like this:

**blog/models.py**
```
from django.db import models
from django.utils import timezone

class Post(models.Model):
        |
        |
        |
```
**class Post(models.Model):**
* **class** is a special keyword that indicates that we are defining an object.
- **Post** is the name of our model. We can give it a different name (but we must avoid special characters and whitespace). Always start a class name with an uppercase letter.
- **models.Model** means that the Post is a Django Model, so Django knows that it should be saved in the database.

# Create tables for models in your database
use this command **python manage.py makemigrations blog**

it will looks like this:

**command-line**
```
python manage.py makemigrations blog
Migrations for 'blog':
  blog/migrations/0001_initial.py:
  - Create model Post
```
*Django prepared a migration file for us that we now have to apply to our database.*

use this command to save the file in our database.

**command line**
```
python manage.py migrate blog
Operations to perform:
  Apply all migrations: blog
Running migrations:
  Rendering model states... DONE
  Applying blog.0001_initial... OK
```
# We create Django admin
To add, edit and delete the posts we've just modeled, we will use Django admin.

*open the file **blog/admin.py** and replace its content with this:*

**blog/admin.py**
```
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```
*OK, time to look at our **Post model**. Remember to run **python manage.py runserver** in the console to run the web server. Go to your browser and type the address http://127.0.0.1:8000/admin/. You will see a login page like this:*

To log in, you need to create a superuser - a user account that has control over everything on the site. Go back to the command line, type **python manage.py createsuperuser**, and press enter.

It look like this:
```
Username: admin
Email address: admin@admin.com
Password:
Password (again):
Superuser created successfully.
```
*Return to your browser. Log in with the superuser's credentials you chose; you should see the Django admin dashboard.*

# Django URLs
Let's open up the **mikku/urls.py** file in your code editor of choice and see what it looks like:

**mikku/urls.py**
```
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
]
```
**mikku/urls.py**
```
path('admin/', admin.site.urls),
```
This line means that for every URL that starts with **admin/**,
# Create first template
Creating a template means creating a template file.

**So first create a directory called templates inside your blog directory.**

**Then create another directory called blog inside your templates directory:**

*And now create a **post_list.html** file (just leave it blank for now) inside the **blog/templates/blog directory.**

It looks like this:
```
blog
└───templates
    └───blog
        ├──post_list.html
```        
# Django views – time to create!
OK, let's open up this file and these line 
```
def post_list(request):
    return render(request, 'blog/post_list.html', {})
```
As you can see, we created a function **(def)** called *post_list* that takes *request* and return a function *render* that will render (put together) our **template blog/post_list.html.**

# Your first Django URL!
Time to create our first URL! We want **http://127.0.0.1:8000/** to be the home page of our blog and to display a list of posts.

# blog.urls
*First Create a new empty file named **urls.py** in the blog directory. All right!*

Here we're importing Django's function url and all of our views from the blog application.

**blog.urls**
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
```
As you can see, we're now assigning a view called post_list to the URL.

**mikku/urls.py**
```
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```
See how your website looks now: http://127.0.0.1:8000/
# Customize your template
*You can now have a little fun and try to customize your template! Here are a few useful tags for that:*

- **<h1>A heading</h1>** *for your most important heading*
- **<h2>A sub-heading</h2>** *for a heading at the next level*
- **<h3>A sub-sub-heading</h3>** *…and so on, up to <h6>*
- **<p>** *A paragraph of text</p>*
- **<em>text</em>** *emphasizes your text*
- **<strong>text</strong>** *strongly emphasizes your text*
- **<br>** *goes to another line (you can't put anything inside br and there's no closing tag)*
- **<a href="https://djangogirls.org">link</a>** *creates a link*
- **<ul><li>first item</li><li>second item</li></ul>** *makes a list, just like this one!*
- **<div></div>** *defines a section of the page*

# Thanku so much
