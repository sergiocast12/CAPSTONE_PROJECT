import mysql.connector
import pandas as pd
import secret

config = {

     'user': secret.user,
     'password': secret.password,
     'host': 'localhost',
     'database': 'creditcard_capstone'

}

db = mysql.connector.connect(**config)
cursor = db.cursor()

#THECONSOLE

input1 = input("Enter Transaction or Customer: ") 
if input1 =="Transaction":
    input1 = input("Enter zip, type or branch: ") 
    if input1 == "zip":
        Month = input("Enter Month: ")
        Year = input("Enter Year: ")
        Zipcode = input("Enter zipcode: ")
        cursor.execute("SELECT CDW_SAPP_CREDIT_CARD.CUST_CC_NO,CDW_SAPP_CUSTOMER.CUST_ZIP, CDW_SAPP_CREDIT_CARD.TIMEID, CDW_SAPP_CREDIT_CARD.TRANSACTION_TYPE, CDW_SAPP_CREDIT_CARD.TRANSACTION_VALUE, CDW_SAPP_CREDIT_CARD.TRANSACTION_ID FROM CDW_SAPP_CREDIT_CARD INNER JOIN CDW_SAPP_CUSTOMER ON CDW_SAPP_CREDIT_CARD.CUST_CC_NO = CDW_SAPP_CUSTOMER.CREDIT_CARD_NO WHERE SUBSTRING(TIMEID, 6, 2) = (%s) AND SUBSTRING(TIMEID, 1, 4) = (%s) AND CUST_ZIP = (%s) ORDER BY SUBSTRING(TIMEID, 9, 2) DESC", (Month, Year, Zipcode) )
        result = cursor.fetchall()
        zip_df = pd.DataFrame(result, columns = ["CUST_CC_NO","CUST_ZIP","TIMEID","TRANSACTION_TYPE", "TRANSACTION_VALUE", "TRANSACTION_ID"])
        print(zip_df)
    if input1 == "type":
        Type = input("Enter Type: ")
        cursor.execute("SELECT TRANSACTION_TYPE, COUNT(TRANSACTION_TYPE) AS NUMBER_VALUES, ROUND(SUM(TRANSACTION_VALUE),0) AS TOTAL_VALUE FROM CDW_SAPP_CREDIT_CARD WHERE TRANSACTION_TYPE = (%s) GROUP BY TRANSACTION_TYPE;", (Type,) )
        result = cursor.fetchall()
        type_df = pd.DataFrame(result, columns = ["TRANSACTION_TYPE","NUMBER_VALUES","TOTAL_VALUE"])
        print(type_df)
    if input1 == "branch":
        Branch = input("Enter Branch: ")
        cursor.execute(" SELECT BRANCH_STATE, COUNT(*) AS TOTAL_NUMBER, ROUND(SUM(TRANSACTION_VALUE),0) AS TOTAL_VALUE FROM (SELECT DISTINCT TRANSACTION_ID, BRANCH_STATE, TRANSACTION_VALUE FROM CDW_SAPP_BRANCH INNER JOIN CDW_SAPP_CREDIT_CARD ON CDW_SAPP_BRANCH.BRANCH_CODE = CDW_SAPP_CREDIT_CARD.BRANCH_CODE ORDER BY TRANSACTION_ID ) AS NEWTABLE WHERE BRANCH_STATE = (%s) GROUP BY BRANCH_STATE", (Branch,))
        result = cursor.fetchall()
        branch_df = pd.DataFrame(result, columns = ["BRANCH_STATE","TOTAL_NUMBER","TOTAL_VALUE"])
        print(branch_df)
if input1 =="Customer":
    input1 = input("Enter check, modify, bill, transaction: ") 
    if input1 == "check":
        ID = input("Enter id: ")
        cursor.execute("SELECT * FROM CDW_SAPP_CUSTOMER WHERE id = (%s)", (ID,))
        result = cursor.fetchall()
        customer_df = pd.DataFrame(result, columns = ["id", "SSN", "FIRST_NAME" , "MIDDLE_NAME" ,"LAST_NAME" , "CREDIT_CARD_NO" , "FULL_STREET_ADDRESS" , "CUST_CITY" , "CUST_STATE" , "CUST_COUNTRY" , "CUST_ZIP" , "CUST_PHONE" , "CUST_EMAIL" , "LAST_UPDATED" ]) 
        print(customer_df)
    if input1 == "modify":
        ID = input("Enter customer id: ")
        Field = input("Choose field to modify : ")
        if Field == "first name":
            first_name = input("Enter new first name: ")
            cursor.execute("UPDATE CDW_SAPP_CUSTOMER SET FIRST_NAME = (%s) WHERE id = (%s)", (first_name, ID))
            db.commit()
            print("Done")
        if Field == "SSN":
            SSN = input("Enter new SSN: ")
            cursor.execute("UPDATE CDW_SAPP_CUSTOMER SET SSN = (%s) WHERE id = (%s)", (SSN, ID))
            db.commit()
            print("Done")
        if Field == "middle name":
            MIDDLE_NAME = input("Enter new middle name: ")
            cursor.execute("UPDATE CDW_SAPP_CUSTOMER SET MIDDLE_NAME = (%s) WHERE id = (%s)", (MIDDLE_NAME, ID))
            db.commit()
            print("Done")
        if Field == "last name":
            LAST_NAME = input("Enter new last name: ")
            cursor.execute("UPDATE CDW_SAPP_CUSTOMER SET LAST_NAME = (%s) WHERE id = (%s)", (LAST_NAME, ID))
            db.commit()
            print("Done")
        if Field == "credit card no":
            CREDIT_CARD_NO = input("Enter new credit card no: ")
            cursor.execute("UPDATE CDW_SAPP_CUSTOMER SET CREDIT_CARD_NO = (%s) WHERE id = (%s)", (CREDIT_CARD_NO, ID))
            db.commit()
            print("Done")
        if Field == "full street address":
            FULL_STREET_ADDRESS = input("Enter new full street address: ")
            cursor.execute("UPDATE CDW_SAPP_CUSTOMER SET FULL_STREET_ADDRESS = (%s) WHERE id = (%s)", (FULL_STREET_ADDRESS, ID))
            db.commit()
            print("Done")
        if Field == "cust city":
            CUST_CITY = input("Enter new cust city: ")
            cursor.execute("UPDATE CDW_SAPP_CUSTOMER SET CUST_CITY = (%s) WHERE id = (%s)", (CUST_CITY, ID))
            db.commit()
            print("Done")
        if Field == "cust state":
            CUST_STATE = input("Enter new cust state: ")
            cursor.execute("UPDATE CDW_SAPP_CUSTOMER SET CUST_STATE = (%s) WHERE id = (%s)", (CUST_STATE, ID))
            db.commit()
            print("Done")
        if Field == "cust country":
            CUST_COUNTRY = input("Enter new cust country: ")
            cursor.execute("UPDATE CDW_SAPP_CUSTOMER SET CUST_COUNTRY = (%s) WHERE id = (%s)", (CUST_COUNTRY, ID))
            db.commit()
            print("Done")
        if Field == "cust zip":
            CUST_ZIP = input("Enter new cust zip: ")
            cursor.execute("UPDATE CDW_SAPP_CUSTOMER SET CUST_ZIP = (%s) WHERE id = (%s)", (CUST_ZIP, ID))
            db.commit()
            print("Done")
        if Field == "cust phone":
            CUST_PHONE = input("Enter new cust phone: ")
            cursor.execute("UPDATE CDW_SAPP_CUSTOMER SET CUST_PHONE = (%s) WHERE id = (%s)", (CUST_PHONE, ID))
            db.commit()
            print("Done")
        if Field == "cust email":
            CUST_EMAIL = input("Enter new cust email: ")
            cursor.execute("UPDATE CDW_SAPP_CUSTOMER SET CUST_EMAIL = (%s) WHERE id = (%s)", (CUST_EMAIL, ID))
            db.commit()
            print("Done")
        if Field == "last updated":
            LAST_UPDATED = input("Enter new last updated: ")
            cursor.execute("UPDATE CDW_SAPP_CUSTOMER SET LAST_UPDATED = (%s) WHERE id = (%s)", (LAST_UPDATED, ID))
            db.commit()
            print("Done")
    if input1 == "bill":
        CREDIT_CARD_NO = input("Enter credit card no: ")
        MONTH = input("Enter month: ")
        YEAR = input("Enter year: ")
        cursor.execute("SELECT CUST_CC_NO, ROUND(SUM(TRANSACTION_VALUE),0) AS MONTHLY_BILL FROM CDW_SAPP_CREDIT_CARD WHERE SUBSTRING(TIMEID, 6, 2) = 11 AND SUBSTRING(TIMEID, 1, 4) = 2018 AND CUST_CC_NO = '4210653312478046' GROUP BY CUST_CC_NO;" )    
        result = cursor.fetchall()
        bill_df = pd.DataFrame(result, columns = ["CUST_CC_NO","MONTHLY_BILL"])
        print(bill_df)

        
    if input1 == "transaction":
        START_DATE = input("Enter start date: ")
        END_DATE = input("Enter end date: ")
        cursor.execute("SELECT CUST_CC_NO, TIMEID, CUST_SSN, BRANCH_CODE, TRANSACTION_TYPE, TRANSACTION_VALUE, TRANSACTION_ID FROM CDW_SAPP_CREDIT_CARD WHERE TIMEID BETWEEN (%s) AND (%s) ORDER BY SUBSTRING(TIMEID, 1, 4) DESC, SUBSTRING(TIMEID, 6, 2) DESC, SUBSTRING(TIMEID, 9, 2) DESC;", (START_DATE, END_DATE) )
        result = cursor.fetchall()
        transaction_df = pd.DataFrame(result, columns = ["CUST_CC_NO", "TIMEID", "CUST_SSN", "BRANCH_CODE", "TRANSACTION_TYPE", "TRANSACTION_VALUE", "TRANSACTION_ID"])
        print(transaction_df)
        

  
else:
    exit(1)
    