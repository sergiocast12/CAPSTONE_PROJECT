# CAPSTONE PROJECT
# ETL process for a Loan Application dataset and a Credit Card dataset

PROJECT DETAILS

*User interacts with the API and CSV data through the console
*When console.py is running, it will display a message "Enter Transaction Or Customer"
*If they enter "Transaction", the user will interact with the Transaction Module
*If they enter "Customer", the user will interact with the Customer Module

Transaction Module

*If "Transaction" is entered, you will get "Enter zip,type or branch"
*For zip you will need to enter month (e.g. 11), year (e.g. 2018), zipcode (e.g. 39120).
*The transactions made by the customer will be displayed
*For type you will need to enter type (e.g. Healthcare)
*The number and total values of transactions for a given type will be displayed
*For branch you will need to enter a branch state (e.g. ny)
*The total number and total values of transactions for branches in a given state will be displayed

Customer Module

*If "Customer" is entered, you will get "Enter check, modify, bill, transaction"
*For check you will need to enter id (e.g. 1)
*The existing account details of the customer will be displayed
*For modify you will need to enter customer id (e.g. 1), field to modify (e.g. first name), enter new value
*The existing account details of the customer would be modified
*For bill you will need to enter credit card no(e.g. 4210653349028689), month (e.g. 11), year(e.g. 2018)
*It will generate a monthly bill for the credit card number for the given month and year
*For transaction you will need to enter a start date (e.g. 2018-01-01), end date (e.g. 2018-11-01)
*The transactions made between two dates will be displayed

TECHNICAL CHALLENGES
-While I was working with the csv data I kept getting duplicate rows which was giving me inaccurate results when querying. At first I thought the data was intentionally like this so I grouped the rows by id to remove the duplicate records. Then I realized that I had been causing the duplicate rows because I was using the append mode when I was loading the data to the database. To fix this I just deleted the tables and created them again and ran the code. I could have used the overwrite mode but at that point I had already grouped the data by id so I just left it like that.  