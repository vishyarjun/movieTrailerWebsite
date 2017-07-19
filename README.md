# Project Movie Trailer

This project lists out some good **movies** and displays it in a web page and allows visitors to browse and watch the trailers

### Pre-Requirements
1. Install Python in the local machine. [Click here, if not already installed](https://www.python.org/downloads/)
2. Create a githib account and Install git in the local machine. [Click here, if not already installed](http://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
> Installation Steps
  1. Fork the github repository. The original repository can be found [here](https://github.com/vishyarjun/movieTrailerWebsite.git)
  2. Clone it to local repository using  `git clone <fork repository url>`
3. Change the directory to the target folder using `cd movieTrailerWebsite`
4. run the program `entertainment_center.py`

### FAQ
1. __How do I run the entertainment_center.py?__
The Program can be run in two ways.
    - Through terminal using `python entertainment_center.py`
    - open IDLE(if installed), **File -> Open -> appropriate folder and choose entertainment_center.py**
2. __Why do I get the following error when I run the entertainment_center.py through terminal?__
```
movieTrailerWebsite/fresh_tomatoes.html" doesn’t understand the “open location” message. (-1708)
70:78: execution error: Can’t get application "firefox". (-1728)
```
This is an issue with MAC recent version and has nothing to do with this entertainment_center.py. Information available [here](https://github.com/jupyter/notebook/issues/2438)


### API
All the movies displayed in the website are obtained by consuming an API from **The Movie DB**. [Click here](https://www.themoviedb.org/) to visit the page.

### Reference
1 [stackoverflow](www.stackoverflow.com)
2 [W3Scools](www.w3schools.com)
3 [The Movies DB](https://developers.themoviedb.org/3)