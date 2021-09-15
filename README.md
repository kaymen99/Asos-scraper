# Asos-scraper

<hr>
<br>
Asos scraper is a simple web application that can run on your computer, it's used to collect products prices data from asos website, it's built using SELENIUM and Flask and provide the following informations in a csv file :

<br>
<ul>
  <li>product name</li>
  <li>product original price(before sales)</li>
  <li>product current price</li>
  <li>product url in asos website</li>
  
</ul>
<br>
To use the web app you need to :
<br>
Install some libraries in your terminal/cmd: <h3>pip install selenium pandas parsel Flask</h3>
<br>

Excute the command in the terminal/cmd : 
<h3>cd asos</h3>
<h3>python app.py</h3>

<br>
You will get a simple page with 3 inputs:
<ul>
  <li>product name : like shoes, shirts,...) </li>
  <li>Gender : choose the product for men or women or unisex </li>
  <li>number of pages : the number of pages to be collected from asos website</li>
</ul>

<br>

After you submit the data will be saved in csv format in the asos directory

