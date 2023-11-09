
![original](docs/media/socio.png)
<!-- <h1 align="center"> The Socio Platform </h1>
<h5 align="center">Let us connect though</h5> -->
<h6 align="Center">

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
 [![git](https://badgen.net/badge/icon/git?icon=git&label)](https://git-scm.com) [![Visual Studio](https://badgen.net/badge/icon/visualstudio?icon=visualstudio&label)](https://visualstudio.microsoft.com) [![HTMX - version 1.8.4](https://img.shields.io/badge/HTMX-version_1.8.4-2ea44f)](https://htmx.org/) [![Made with  - JavaScripts](https://img.shields.io/badge/Made_with_-JavaScripts-blueviolet)](https://www.javascript.com/) [![Bootstrap - 4.4.1](https://img.shields.io/badge/Bootstrap-4.4.1-ff69b4)](https://getbootstrap.com/docs/3.4/)

</h6>

<br>

<h4 align="center">
<a href="https://github.com/yeazin/The-Socio?tab=readme-ov-file#-project-installation-"> Project Installation</a> | 
<a href="https://github.com/yeazin/The-Socio?tab=readme-ov-file#project-flow"> Project Flow </a>
|<a href="https://github.com/yeazin/The-Socio?tab=readme-ov-file#-project-documention-"> Project Documention </a>

</h4> 

<br>


<h2 align="center"> Project Installation </h2>
<br>

#### Clone the repository using the following command

```bash
git clone https://github.com/yeazin/The-Socio.git
# After cloning, move into the directory 
# having the project files 
```
#### Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env

# Use this on Linux and Mac
python3 -m venv env
```
#### Activate the virtual environment

```bash

# Windows
env\Scripts\activate

# Linux and Mac
source env/bin/activate

```
#### Go the project folder and Install all the project Requirements

```bash

# Windows
pip install -r requirements/dev_requirements.txt

# Linux and Mac
pip3 install -r requirements/dev_requirements.txt

```

#### Run the Following Script before makemigrations otherwise an error will occur

```bash
# As we have a logging system We need to create the logs file first

# Windows 
py create_log.py

# Linux & Mac
python3 create_log.py
```

#### Apply migrations and create your superuser (follow the prompts)

```bash

# apply makemigration 
python manage.py makemigrations

# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser

```

#### Run the development server

```bash
# run django development server

# Windows 
py manage.py runserver

# Linux & Mac
python3 manage.py runserver

```
Now we are good to Go . We can check the [127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)<br> and we can access the admin panel.
[ NB : Create a Profile from the admin panel then we can login in client side with <br> the same credentials  otherwise it will show an
error "User has no Profile"]
<br>

<h2 align="center">Project Flow</h2>
<br>

#### Project Structure 
<br>

```bash 

    docs/ # docs file of the Project

    requirements/
        |-- dev_requirements.txt # Requirements for the project

    socio/
        |__ config/  #Root Config folder
            |-- __init__.py
            |-- settings.py # All the settings 
            |-- urls.py (Root URL file)
            |-- wsgi.py
            |-- asgi.py
        
        |__ accounts/
            |-- __init.py
            |-- models # database folder  
            |-- views 
            |-- serializer.py # API file
            |-- urls.py # accounts URL file)
            |-- admin.py

        |__ post/
            |-- __init.py
            |-- models # database folder  
            |-- views 
            |-- serializer.py # API file
            |-- urls.py # accounts URL file)
            |-- admin.py

        |__ profile/
            |-- __init.py
            |-- models # database folder  
            |-- views 
            |-- serializer.py # API file
            |-- urls.py # accounts URL file)
            |-- admin.py

        |__ util_base/
            |__ models/ # models file of abstraction
                |-- _initModels.py
            |__ serializer/
                |-- _initSerializer.py

    |-- create_log.py # an Script file to create logs file  
    |-- .gitignore
    |-- readme.MD 
    

```
<br>

<h2 align="center"> Project Documention </h2>

#### Thanks for Tagging alone with the Technical Documention , Read the [Project Documtion here](https://github.com/yeazin/Project-Coding-Pari-Na/tree/main/docs#-coding-pari-na-documention-) 

Project Documention URL :  [https://projectcodingparina.docs](https://github.com/yeazin/Project-Coding-Pari-Na/tree/main/docs#-coding-pari-na-documention-)

Wish you a Great Time ...

If you have any quiry regarding this project <br>
Feel free to contact me :

Email : naz.yeasin@gmail.com