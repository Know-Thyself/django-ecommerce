# Django E-commerce

[![Screenshot of the storefront of the website.](/static/media/images/site-screenshot.png)][Sustainability E-commerce website live link]

I've built this **Sustainability E-commerce** Full Stack Web Application as part of my learning journey and practicing **Python** and **Django Web Framework**.

Building this project has thought me a lot of new skills and introduced me to a variety of new technologies.

Although I am new to Django, I am very much familiar with Web Development in languages I am much more proficient at such as _JavaScript_, _React.js_, _Next.js_, _Node.js_, _HTML_ and _CSS_ along with related _Frameworks_ and _Libraries_ as well as _PostgreSQL_.

My prior knowledge of _HTML_, _CSS/Bootstrap_, _JavaScript_ and _PostgreSQL_ have served me well in building this **Django E-commerce** web app as they are some of the technologies I used for this project.

## Understanding The Project Structure

The main project is called **ecommerce** and can be found in the _ecommerce_ directory. I've integrated four django apps in this project, namely: _store_, _account_, _cart_ and _payment_. These apps are responsible for handling different aspects of the project that are correlated to what their individual names suggest.

The _ecommerce_ directory contains important settings, configurations and urls/routes/paths or entry points to the apps to enable us run all of them as one web application smoothly. Having a look at _settings.py_ and _urls.py_ in the _ecommerce_ directory could give you a better idea as to how the project is structured.

## Live Link

Feel free to click this link or the image at the top of this page to visit the live website [Sustainability E-commerce][Sustainability E-commerce website live link].


Please bear in mind that loading the site initially might be slow as it is deployed using free tiers of render web service and elephantSQL database. However, once the initial loading is complete, everything runs efficiently and swiftly.


## Installing Project Requirements and Running the App Locally

If you are interested in cloning and running the app locally, you need to install the libraries, modules and frameworks that are listed in the *requirements.txt* file.

### Installation

Assuming you've already installed *Python* and *Pip* and *virtual environment* has already been configured on your machine, you can install all of the project requirements/dependencies by simply running the following command.
```
pip install -r requirements.txt
```

### Running the app locally

> ### Step 1. 
> Running the app locally can be a bit tricky as it involves creating and loading your own *environment variables* consisting of your credentials and secret keys.
> #### The essential **environment variables** are:
> + DATABASE_URL
> + CART_SESSION_KEY
> + SECRET_KEY
> + EMAIL_BACKEND
> + EMAIL_HOST
> + EMAIL_HOST_USER
> + EMAIL_HOST_PASSWORD
> + EMAIL_PORT
> + ALLOWED_HOSTS
> + SANDBOX_CLIENT_ID
> + PYTHON_VERSION
> + DEBUG

> Of course, you can rename these *environment variables* however you want.

>### Step 2.
> Run the following command to migrate database models that are defined in each app's ***models.py*** files and are prepared to be migrated from ***migrations*** directories of ***account***, ***cart***, ***payment*** and ***store*** django apps to your local or remote database. 
```
python manage.py migrate
```

> ### Finally
> Once the data migration is successful, You can simply run the following command and follow your local host link to see the web app in action.
```
python manage.py runserver
```





[Sustainability E-commerce website live link]: https://sustainability-ecommerce.onrender.com/