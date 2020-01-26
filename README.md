### A teachers tool
## Heymo89

##Installation
------------------
To make your own setup of the project
 you will need to
  * Have your own google account, like a gmail
  * go to console.cloud.google.com
  * activate APIs "Google drive" and "Google Sheets API"
  * and download a json file containing your credentials.
  * then share your google drive sheet with your "client-email" listed in your credentials

## Running / testing functions
----------------------------------
this is an ongoing project.
So right now it takes simple commands
like adding

### adding student alphabetically
run with :
>> python3 actions.py

Adds a student name at the bottom of the student list in the google sheet.
Will then make a list of all names, make a dictionary with all student information, key student name. Sorts name list  by default python .sort(). Removes rows before updating cells.
