import streamlit as myapp
import sqlalchemy as crt
conn = crt.create_engine("postgresql://postgres:Zhaksylyk27@db.knpfibpenimaqbaqyame.supabase.co:5432/postgres")
#password = 'Zhaksylyk27'
conn.connect()

def readeverything(tables):
    read = crt.text(f"SELECT * FROM {tables}")
    return conn.execute(read)

def main():
    myapp.title("Assignment2")
    menu = ["Create","Read","Update","Delete"]
    option = myapp.sidebar.selectbox("Functions",menu)
    tables = ["DiseaseType","Country", "Disease", "Discover", "Users", "PublicServant", "Doctor", "Specialize", "Record"]
    option_tables = myapp.sidebar.selectbox("Tables",tables)

    if option == "Create":
        if option_tables == "DiseaseType":
            tid = myapp.number_input("Enter the ID: ", step=1)
            description = myapp.text_input("Enter the description: ", max_chars=140)
            if myapp.button("Add DiseaseType"):
                inserttype = crt.text(f"INSERT INTO DiseaseType VALUES ({tid},'{description}')")
                conn.execute(inserttype)
        elif option_tables == "Country":
            cname = myapp.text_input("Enter the country name: ", max_chars=50)
            population = myapp.number_input("Enter the number of population: ", step=1)
            if myapp.button("Add Country"):
                insertcou = crt.text(f"INSERT INTO DiseaseType VALUES ('{cname}','{population}')")
                conn.execute(insertcou)
        elif option_tables == "Disease":
            discode = myapp.text_input("Enter the disease code: ", max_chars=50)
            pathogen = myapp.text_input("Enter the pathogen: ", max_chars=20)
            tid = myapp.number_input("Enter the ID: ", step=1)
            description = myapp.text_input("Enter the description: ", max_chars=140)
            if myapp.button("Add Disease"):
                insertdis = crt.text(f"INSERT INTO Disease VALUES ('{discode}','{pathogen}',{tid},'{description}')")
                conn.execute(insertdis)
        elif option_tables == "Discover":
            cname = myapp.text_input("Enter the country name: ", max_chars=50)
            discode = myapp.text_input("Enter the disease code: ", max_chars=50)
            first_enc_date = myapp.date_input("First encounter date: ")
            if myapp.button("Add Discover"):
                insertdisc = crt.text(f"INSERT INTO Discover VALUES ('{cname}','{discode}','{first_enc_date}')")
                conn.execute(insertdisc)
        elif option_tables == "Users":
            email = myapp.text_input("Enter the user's email: ",max_chars=60)
            name = myapp.text_input("Enter the user's name: ",max_chars=30)
            surname = myapp.text_input("Enter the user's surname: ",max_chars=40)
            salary = myapp.number_input("Enter the user's salary", step=1)
            phone = myapp.number_input("Enter the user's phone number: ", step=1)
            cname = myapp.text_input("Enter the country: ",max_chars=50)
            if myapp.button("Create User"):
                insertuser = crt.text(f"INSERT INTO Users VALUES ('{email}','{name}','{surname}',{salary},{phone},'{cname}')")
                conn.execute(insertuser)
        elif option_tables == "PublicServant":
            email = myapp.text_input("Enter the public servant's email: ",max_chars=60)
            department = myapp.text_input("Enter the name of the department: ",max_chars=50)
            if myapp.button("Create PublicServant"):
                insertpublic = crt.text(f"INSERT INTO PublicServant VALUES ('{email}','{department}')")
                conn.execute(insertpublic)
        elif option_tables == "Doctor":
            email = myapp.text_input("Enter the doctor's email: ",max_chars=60)
            degree = myapp.text_input("Doctor's degree: ",max_chars=20)
            if myapp.button("Create Doctor"):
                insertdoctor = crt.text(f"INSERT INTO Doctor VALUES ('{email}','{degree}')")
                conn.execute(insertdoctor)
        elif option_tables == "Specialize":
            id = myapp.number_input("Enter the ID of disease: ",step=1)
            email = myapp.text_input("Enter the email of doctor: ",max_chars=60)
            if myapp.button("Create Specialize"):
                insertspec = crt.text(f"INSERT INTO Specialize VALUES ({id},'{email}'")
                conn.execute(insertspec)
        elif option_tables == "Record":
            email = myapp.text_input("Enter the email of public servant: ",max_chars=60)
            cname = myapp.text_input("Enter the country in which the public servant records: ",max_chars=50)
            disease_code = myapp.text_input("Enter the disease code: ",max_chars=50)
            total_deaths = myapp.number_input("Enter the total number of deaths: ",step=1)
            total_patients = myapp.number_input("Enter the total number of patients: ",step=1)
            if myapp.button("Create Record"):
                insertrec = crt.text(f"INSERT INTO Record VALUES ('{email}','{cname}','{disease_code}',{total_deaths},{total_patients})")
                conn.execute(insertrec)
    elif option == "Read":
        myapp.subheader("View page")
        if option_tables == "DiseaseType":
            myapp.table(readeverything("DiseaseType"))
        elif option_tables == "Country":
            myapp.table(readeverything("Country"))
        elif option_tables == "Disease":
            myapp.table(readeverything("Disease"))
        elif option_tables == "Discover":
            myapp.table(readeverything("Discover"))
        elif option_tables == "Users":
            myapp.table(readeverything("Users"))
        elif option_tables == "PublicServant":
            myapp.table(readeverything("PublicServant"))
        elif option_tables == "Doctor":
            myapp.table(readeverything("Doctor"))
        elif option_tables == "Specialize":
            myapp.table(readeverything("Specialize"))
        elif option_tables == "Record":
            myapp.table(readeverything("Record"))
    elif option == "Update":
        myapp.subheader("Update details")
    elif option == "Delete":
        if option_tables == "DiseaseType":
            myapp.subheader("Delete from table")


        
if __name__ == '__main__':
    main()






    