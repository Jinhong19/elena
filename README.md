# elena

## Dependencies
### For Mac OS user
Create and activate virtual environment  
`python3 -m venv venv`  
`source venv/bin/activate`

Install dependencies  
`pip3 install -r requirements.txt`

### For Windows user
Create and activate virtual environment  
Invoke the venv command as follows:  
`c:\>c:\Python35\python -m venv c:\path\to\myenv`  
Alternatively, if you configured the PATH and PATHEXT variables for your Python installation:  
`c:\>python -m venv c:\path\to\myenv`  
And then activate the virtual environment  
`source venv/bin/activate`

Install dependencies  
`pip install -r requirements.txt`
You may need to also install the [Build Tools for Visual Studio 2019](https://visualstudio.microsoft.com/downloads/)

## Run Server Locally
`python3 Back-End/server.py`

## Open in browser
open in a browser: Fron-End/main.html

## Screenshots
Search for shortest route(100%) with minimum elevation gain  
![100% minimum screenshot](https://github.com/Jinhong19/elena/blob/master/images/min_100.png)

Search for a route that is not longer than 160% of the shortest route and with maximum elevation gain  
![160% maximum screenshot](https://github.com/Jinhong19/elena/blob/master/images/max_160.png)

Search for a route that is not longer than 200% of the shortest route and with maximum elevation gain  
![200% maximum screenshot](https://github.com/Jinhong19/elena/blob/master/images/max_200.png)

Limitation: Make sure location inputs are in the database(Amherst Center, MA area), see Testing/Testing.py for query examples.