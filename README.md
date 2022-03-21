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

<h3>How to run :</h3>

<b>Clone this repo: </b>

```git clone https://github.com/Aymen1001/Asos-scraper.git```

<b>Install the required libraries: </b>

```pip install selenium pandas parsel flask```
<br>

Excute the command in the terminal/cmd : 

```cd Asos-scraper/asos```

And then: 

```python app.py```

<br>
You will get a simple web page with 3 inputs:
<ul>
  <li>product name : like shoes, shirts,...) </li>
  <li>Gender : choose the product for men or women or unisex </li>
  <li>number of pages : the number of pages to be collected from asos website</li>
</ul>

<br>

After you submit the data will be saved in csv format in the asos directory

