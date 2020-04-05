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
$git curl http://riverside-covid.herokuapp.com/city/Riverside 
```

This will give you:
```json
    [
    {
        "attributes": {
            "NAME": "Riverside",
            "NAMELSAD": "Riverside city",
            "OBJECTID": 1,
            "Point_Count": 33,
            "SUM_Deceased": 0,
            "Shape__Area": 0.0206009713788262,
            "Shape__Length": 1.06927396949517
        }
    }
]
```


Where "Point_Count" is the number of cases within that city.

For cities that have a space in the name such us "Moreno Valley" you will have to enter the name with a hypen: "Moreno-Valley".

# If you would rather not see everything in a JSON format, you can user this link: https://riverside-covid.herokuapp.com/city-list
This will return a string of all the cities within the county in alphabetical order, displaying the name followed by the current cases count an death count in that city.


### Try it out

All you need to run this project on your computer is git and an IDE of your choice that can run Python applications. I am using IDLE to write this. You can download Python from here https://www.python.org/downloads/.

To clone this project, what I did first was create a folder on my machine where I wanted to download the project to. Then, copy the directoy of the folder that you just created. 
Open a terminal and "cd" into the folder. Then follow the steps below:

```sh
$git init
$git pull https://github.com/Abruuham/RiversideCovidCases.git
```

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
