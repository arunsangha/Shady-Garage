<h1>Shady Garage</h1>
<p>This project came alive when we saw that the car society had no platform covering one thing, and that one thing was meets.
The project is a website buildt with Django as the backend technology. Other technologies you will find in this project is:
<ul>
<li> Ajax </li>
<li> Jquery </li>
<li> Javascript </li>
<li> HTML </li>
<li> CSS </li>
<li> Bootstrap </li>
</ul>
</p>

<h2>Getting Started</h2>

These instructions will get you a copy of the project up and running on your local machine for testing purposes.

<h3>Prerequisites</h3>
<ul>
<li> Anaconcda or Miniconda installed. - https://anaconda.org</li>
<li> Python 3.6.2 or higher. - https://www.python.org/downloads/release/python-362/</li>
<li> Django 1.11.8. - https://django-activity-stream.readthedocs.io/en/latest/installation.html </li>
<li> An editor(For example: Atom). - https://atom.io </li>
</ul>

<h3>Installing</h3>
<ul>
  <li><h5>Step 1</h5>
  <p>After you have fulfilled all the prerequisites, clone the project: "https://github.com/arunsangha/Shady-Garage.git"</p></li>

  <li>
  <h5>Step 2</h5>
  <p>Open a terminal and create a conda enviroment:<br>
    "conda create --name shadyGarage django=1.11.8".<br>
    Activate the newly created enviroment: "activate shadyGarage" or for linux and mac users "source activate shadyGarage"</p>
  </li>
  
   <li><h5>Step 3</h5>
    <p>Pip install all these packages (sorry, we should have had a requirments file):<br></p>
    <ul>
      <li>djangorestframework</li>
      <li>django-bootstrap3</li>
      <li>Faker</li>
      <li>misaka</li>
      <li>Pillow</li>
      <li>piexif</li>
      <li>sorl-thumbnail</li>
    </ul>
  </li>
  
   <li>
  <h5>Step 4</h5>
   <p>Create a stripe account and add the keys to local.py and cart-checkout.html<br>
   </p>
  </li>
  <h5>Step 5</h5>
   <p>Check if the settings __init__.py file has "try: from .local import *".<br>
      The file is in the ShadyGarage folder.
   </p>
  </li>
 
   <li>
  <h5>Step 6</h5>
   <p>Now run "python manage.py runserver". </p>
  </li>
  
</ul>


<h2>Authors</h2>
<ul>
  <li><h5>Arun Sangha - Fullstack <H5></li>
  <li><h5>Christian Thorby - Frontend </h5></li>
</ul>

<h2>License</h2>
Copyright © 2017, Shady Garage.
