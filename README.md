# Eazy-Shopper #

* The shopping list manager is an application like a  shopping bot that allows the user to input data and manipulate it according to the user choices and the shopping bot outputs a result based on user choices and input.

* The aim of this program is to help user have a proper planning with shopping list record,
 this  shopping list app is beneficial to users in a lot of ways. 
 First, a user will likely make an improptu decision to impulse buy a product that was never in the plan, this kind of uncontrolled urge will definitly impact the user financially, which the ripple effect can spread all the way to incur debt , it can also be a detriment to a once healthy credit score. However, having a proper planning of the items you want to buy could come in handy as it will help in avoiding over spending, and impulse buying by helping user to focus on what is really needed.

* Secondly, the shopping list program saves user time and energy, not having a list of what to buy at the store makings shopping a headache and time consuming as wider product choices can be a distraction which can be overwhelming sometimes, but if you already have the choice of items you which to buy makes shopping very easy and less time consuming. In the same vein, having a shopping list reduces waste in the sense that when you buy things you do not really need immediatly it most times end up in the trash.

* Further more, it can help in improving user memory and helps user to focus and have proper planning of things.

![title and logo screen](/images/title.png)



## Features
_______________________________

## Greeting

*  The first thing a user sees when the program is been executed is a display of the program title with a design.

* It asks the user to input a name which is then displayed as a greeting.


![morning](/images/greetings2.png)

![evening](/images/greetings.png)



## Option Menu 
* This is a section that shows  to the user  the options available to choose from. 

* This option ranges from 1 to 7.

* Based on user selection the program execute each task accordingly.
	




![Option Menu](/images/optionmenu.png)



## Option 1: Add item to list.

* This option allow user to add items to the list.
* It also tells the user if an item has already been added to avoid repetition.




![Option Menu 1a](/images/option1a.png)

![Option Menu 1b](/images/option1b.png)



## Option 2: View List

* This option displays the content of the list. 

* If nothing was previously added,  it displays "List is empty, try adding adding an item".



![Option Menu 2a](/images/option2a.png)

![Option Menu 2b](/images/option2b.png)



## Option 3: Total number of items in the list

* This option displays the total number of items on the list. 

* Displays "0" if the list is empty


![Option Menu 3](/images/option3.png)


## Option 4: Find items in the list
	
* The find item in the list option searches the list for a user specified item name, which then search and return a message if the item is found or not 


![Option Menu 4a](/images/option4a.png)

![Option Menu 4b](/images/option4b.png)


## Option 5: Delete items from the list

* The delete item from the list option also searches the list for a user specified item name, which then search and delete the item if found on the list or not.


![Option Menu 5a](/images/option5a.png)

![Option Menu 5b](/images/option5b.png)



## Option 6: Empty  the list

* This erase every content of the list and return it back to an empty list.
* It prints a message based on if the list is already empty or not.

![Option Menu 6a](/images/option6a.png)

![Option Menu 6b](/images/option6b.png)

## Option 7: Exit program

* This function allows user to exit the program.
* It gives the user an option to chose either to exit or run the program again from the beginning.
* It also print a thank you message to the user based on the time of the day.

![Option Menu 7](/images/option7a.png)

## Testing

* This program was properly tested using Pep8 online [Pep8](https://www.http://pep8online.com/checkresult "pep8") .

* All the generated errors like "trailing white spaces and no newline at the end of file were rectified.

* I confirm that all the functionality of this program works perfectly.

![Footer section](/images/pep8.png)
## Tools used

## Language
* Python

## Other program used: 
* Gitpod:
    * Gitpod: A versatile IDE used to code the program [Gitpod](https://www.gitpod.io/ "gitpod")

* Github:
    * Github: a platform used for storing, tracking, and collaborating on software projects  [Github](https://www.github.com/ "github")

* Git:
    * Git: Used for version control.

* Pep8:
    * pep8: an online python code checker  [pep8](https://http://pep8online.com/checkresult/ "pep8")

* Heroku:
    * Heroku: used in the deployement of the program  [Heroku](https://http://heroku.com/ "Heroku")



## Bugs
* No bugs was found as at the time of deployment.


##  User Input Validation.

* User input validation
	* The program code was written in a way that it controls any invalid user data input, It allows inputs like "Peanut butter", "Scottish- Whiskey". The error messages were controlled by use of various conditional statements.

## Deployment

* The program was deployed to Heroku by following this steps.

* On the Heroku wesbite, create an account.

* After signing in into your account click on create new app button.

* Chose a unique name for the application to be deployed.

* Chose a region.

* Click on settings.

* Navigate to Config var.

* In the Key Value space we need to input PORT for KEY must be in capitals and 800 for PORT

* Click add.

* Click add buildpack, choose python first save changes and add nodjs must be in this order.

* Navigate to the deploy tab on the menu.

* Chose your choice of deployment github is the choice for this project.

* Enter your github repository name and search, if found then click connect.

* Chose to either deploy automatically or manually.

* On this project, our choice is manual deployment, click and wait until a message appear confirming that the application was successfully deployed.

* Click on view app button to run the application.


* The Live link to the deployed program on Heroku [Shopping list](https://https://shopping-list-v01.herokuapp.com/ "shopping list manager").

* The github link is  [Shopping list](https://github.com/gullah26/shopping_list "shopping list manager").

## Credits

* Content

	* Insipiration was drawn  from  [Geek tutorials](https://www.youtube.com/watch?v=9-jazqksAnA "geek tutorials")

    * Insipiration to structure the flow  [Richard](https://gist.github.com/richardbwest/d0365ebb89e89e7290e7cdb9cbc95530 "Richard")

    * Some of the code to validate user data input was from [ Mrst12 ](https://github.com/Mrst12/shop-app#programmes-used "Mrst12")

    The aim of the app inspiration was from [ Positive lending solution ](https://www.positivelendingsolutions.com.au/resources/information-centre/8-reasons-to-make-a-shopping-list/ "positive-lending-solution")


    ## Acknoledgements

    *  Codeinstitute , the slack community, and Codeinstitue mentor support team