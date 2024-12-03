# AD's Michael Kors PopUp
*By Amelia Soucy and Desayna Christmas*

## Project Proposal
**Title:** AD's Michael Kors PopUp

**Members:** Amelia Soucy and Desayna Christmas 

**Objective:** Through this project, our goal is to provide a platform where consumers can easily view 10 different Michael Kors purses and ultimately add one (or many!) to their cart. Our visually appealing HTML page will list, describe, and depict the purse options, as well as calculate the total price of purses added to customers' carts via a FastAPI.

**Tech Stack and Resources:** 
- Demo code and notes from our class sessions:
    - HTML pages, CSS styling, and JavaScript demos
    - Amazon example 
    - API and JSON demos
    - Bitcoin and 404 FastAPI examples
- Homeworks:
    - Homework – Python Programming 1
    - Homework - Python Programming 2
    - Homework – API
    - Homework – Web
- Michael Kors website: https://www.michaelkors.com/women/handbags/
- HTML online editor: https://www.w3schools.com/html/html_editor.asp
- ChatGPT
- Professor Li's insight/demos/answers to our questions via Slack and WebEx

## Project Overview
Through this project, our goal is to provide a platform where consumers can easily view 10 different Michael Kors purses and ultimately add one (or many!) to their cart. Our visually appealing HTML page will list, describe, and depict the purse options, as well as calculate the total price of purses added to customers' carts via a FastAPI.

## Usage Guidelines
Users can browse through our limited inventory of hand selected bags, read the description, look at the price and add to cart if they decide to buy the bag. Users are also able to look at their cart and see the total amount of their purchase. 

## Dependencies
Libraries:
- fastapi (FastAPI and Request classes)
- fastapi.responses (HTMLResponse class)
- fastapi.exceptions (HTTPException class)
- os
- json 

## Project Structure
The main.html is the front page of our website. The cart page is also another page users can click on to view their purchase amount. The CSS and JS files connect to the html pages for styling and creating "add to cart" buttons. The cart calculator connects to the web page in order to calculate the total amount of items. The 404 error page is also connected to the webpage in order to provide a customized error screen. The JSON file stores the database of purses and their prices. 


## Collaboration Information
Amelia and Desayna collaborated well to complete this project! While we were in constant communication (via iMessage and WebEx) throughout and finished the project together to link the back- and front-end code, our individual responsibilities were generally as follows:

- Amelia: back-end code, including creating the data file in json, creating the images folder with all 10 purse images locally stored, and building out the cart calculator functions and 404 error FastAPI in Python

- Desayna: front-end code, including building out the HTML main and cart pages, as well as creating and implementing a CSS stylesheet and JavaScript features

## Acknowledgements
In addition to the aforementioned libraries (listed in the "Dependencies" section), we used the following resources to complete this project:

- ChatGPT
- Assistance from Professor Li via Slack and WebEx
- Homeworks and in-class demos
- Examples and information publicly available on GitHub

## Reflection
Overall, we really enjoyed working together on this project! It was fun to implement bits and pieces of class examples, while also exploring new code and writing code from scratch. This project definitely tied together our understanding of the different aspects we learned throughout the semester, such as how a json API can be used as data for an HTML page.

That said, we did have trouble connecting the back-end and front-end aspects when implementing a cart calculator. We found ChatGPT helpful for answering some questions, but the examples it gave often weren't specific to our unique situation. This made it hard for us to draw information from it, as it was very vague and did not work well with code we already had. This was important to notice, proving that ChatGPT should be used as a tool for assistance, not verbatim.

In terms of the future, we learned hard projects like this require the use of many resources: in this case, online tools, demos from class, and help from Professor Li. We also learned how much trial-and-error goes into developing original coding projects, as we were constantly making changes, testing those changes to see how they worked, and researching/using demo code from class to help make our changes work. This got very frustrating at times, but it was definitely important to experience in terms of knowing to have patience and to persist in future endeavors like this.
