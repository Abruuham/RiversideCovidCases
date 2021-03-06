# Riverside Covid-19 Cases

This project was written in Python in order to document the number of COVID-19 cases that are in the cities of Riverside County:

  - Tracking daily coronavirus case number
  - Allow users to call an API to download results
  *DISCLAIMER: All information is currently being gathered from the riverside city website [riverside-web]


### Tech

This project is solely using the Python programming language. I also used Flask, for this project.
**Install Flask:**
```sh
$pip install flask
```

### API Usage

To use the API for your own projects, you can use this link: https://riverside-covid.herokuapp.com/city/{string}
Just change the string to the name of the city that you want to track. The names must be capitalized in order to work properly.
If you want to pull all data down for all cities, just use the number 0 as the string.


```sh
$curl http://riverside-covid.herokuapp.com/city/Riverside 
```

This will give you:
```json
    [
    {
        "attributes": {
            "NAME": "Riverside",
            "NAMELSAD": "Riverside city",
            "OBJECTID": 1,
            "Point_Count": 10329,
            "SUM_Deceased": 233,
            "SUM_Recovered": 9076,
            "Shape__Area": 0.0206009713692765,
            "Shape__Length": 1.06927397901312
        }
    }
]
```


Where "Point_Count" is the number of cases within that city.

For cities that have a space in the name such us "Moreno Valley" you will have to enter the name with a hypen: "Moreno-Valley".

**If you would rather not see everything in a JSON format, you can use this link: https://riverside-covid.herokuapp.com/city-list**
This will return a string of all the cities within the county in alphabetical order, displaying the name followed by the current cases count an death count in that city.


### Try it out

All you need to run this project on your computer is git and an IDE of your choice that can run Python applications. I am using IDLE to write this. You can download Python from here https://www.python.org/downloads/.

To clone this project, what I did first was create a folder on my machine where I wanted to download the project to. Then, copy the directoy of the folder that you just created. 
Open a terminal and "cd" into the folder. Then follow the steps below:

```sh
$git init
$git clone https://github.com/Abruuham/RiversideCovidCases.git
```
Open the project in your ide of choice, I am using Visual Studio Code with the live server extension. 
If you prefer to run from the terminal then you can simply type:
```sh
$python3 covidAPI.py
```
This will help us run the API. One running on the local host, you can use any of the following links to get view the data:
- localhost:{port}/city/0 - this will return the data for all cities as a json array
- localhost:{port}/city/{city name} - the city name will depend on the city that you are looking for. Currently, only cities in Riverside county are shown. This means you can write the following cities: Riverside, Hemet, Menifee, Murrieta, etc.. If the city has two names such as French Valley, you will need to add a hyphen instead of a space such as French-Valley
- localhost:{port}/city/allcases - this will simply return a number with all the cases
- localhost:{port}/city/alldeaths - this will simply return a number with all the deaths
And that is it!

If you dont want to use git, then just click on the "clone or download" button and download the .zip file to your computer.





License
----

MIT

**Just for Fun!**

Feel free to follow me on [instagram] or on my [linked in]! I'm still and always will be learning and practicing new ways of programming so if you have any suggestions, please message me and help me learn something new!

**Programming, Hell Yeah!**



   [riverside-web]: https://www.rivcoph.org/coronavirus
   [git-repo-url]: <https://github.com/Abruuham/RiversideCovidCases.git>
   [linked in]: <https://www.linkedin.com/in/abraham-calvillo/>
   [instagram]: <https://www.instagram.com/abruuh_ham>
   [python]: <https://www.python.org/downloads/>
