Code Review 1: Intro to Python
Today’s code review has two parts: showing off your Python skills, and filling out the demographic information questionnaire.

Grading Policy
This is a solo project. You're encouraged to do online research, but you may not collaborate with classmates, and all the code must be your own. Plagiarized work may result in expulsion.

For details on code review policy, please see the ‘Code Review Assessment Projects’ section of the ‘School Policies’.

Submissions

Create a GitHub repository for part 1 of this code review, and email a link to the repository to hello@datastack.academy by 5pm PST tomorrow (Saturday). Please include the subject line “CR 1: Intro to Python”.
Part 1 Instructions
Please stick to the function names given below, so that the code review can be graded with automated testing.

Setup Git
As always, create a repository on GitHub for this project.
Include an informative README, a .gitignore file, a requirements.txt file, and at least 8 commits.

Write the following in a file called main.py or a notebook called main.ipynb:

1. A function called fourth_place() that takes a list as an argument.

fourth_place() should return the fourth item in the list
Use try/except to catch IndexErrors



2. A function called dict_sayer() that takes a dictionary as an argument.

dict_sayer() should check whether the dictionary is empty (i.e. an empty dictionary looks like this: `{}`)


If the dictionary isn't empty (i.e. there are one or more items in it):
print a string for each item saying the name of each key and its value
return the Boolean True
If the dictionary is empty:
print a string saying that the dictionary is empty
return the Boolean False



3. Write a function called galaxy(). galaxy() should take:

a positional argument of the user's home planet, followed by
a varying number of arguments (**args), and
a keyword argument of pluto_is_planet, which defaults to a Boolean of your choice.
galaxy() should put all the arguments into a string, and return that string.

Below the function definition, call galaxy(). For the varying number of arguments, name as many planets as you can.



4. Include a docstring for each of the functions above.

5. Define a class called `Cat`. `Cat` should have:

An attribute of `color`
An attribute of `name`
A method called `meow` that prints “Mmmrreow!”

6. Create a cat instance, and use dot notation to show its name.

7. Create a second cat instance, and use dot notation to call its meow method.

Graded Criteria
In order to pass a code review, all of the graded criteria must pass.


Include an informative README, a .gitignore file and at least 8 commits.
The project should be well-commented, without unused code.
fourth_place is completed, and runs according to the specs.
dict_sayer() is completed, and runs according to the specs.
galaxy() is completed, and has been called with all the needed arguments.
Each function contains a docstring.
The Cat class is correctly defined.
Two cat instances are created.
One cat instance uses dot notation to show an attribute, the other calls a method.
The demographic questionnaire is completed.
