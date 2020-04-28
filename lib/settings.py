import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

token = "1238492927:AAFbniUq4oby9XtN3kuzxYpMnbmWWewG2hM"


def Connect_to_Database():
    mydb = psycopg2.connect(database="postgres", user="postgres",
                            password="root", host="127.0.0.1", port="5432")
    mydb.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE Health;")
    mydb.commit()
    print("Database has been created successfully !")
    return mydb


def add_corona(Country, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered):
    mydb = psycopg2.connect(database="Health", user="postgres",
                            password="root", host="127.0.0.1", port="5432")
    mycursor = mydb.cursor()
    mycursor.execute(' Health;')
    sql = "CREATE TABLE IF NOT EXISTS Covid_19 (id INT PRIMARY KEY,Country VARCHAR(255),Slug VARCHAR(255),NewConfirmed INT NOT NULL, TotalConfirmed INT NOT NULL,NewDeaths INT NOT NULL ,TotalDeaths INT NOT NULL,NewRecovered INT NOT NULL,TotalRecovered INT NOT NULL)"
    mycursor.execute(sql)
    sql = "INSERT INTO Covid_19 (Country,Slug,NewConfirmed,TotalConfirmed,NewDeaths,TotalDeaths,NewRecovered,TotalRecovered ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (Country, Slug, NewConfirmed, TotalConfirmed,
           NewDeaths, TotalDeaths, NewRecovered, TotalRecovered)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    print(mycursor.rowcount, "Case added")


def Show_Cases():
    mydb = psycopg2.connect(database="Health", user="postgres",
                            password="root", host="127.0.0.1", port="5432")
    mycursor = mydb.cursor()
    sql = "SELECT Country , TotalConfirmed FROM Covid_19 ORDER BY TotalConfirmed"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for item in myresult:
        print(item)
    print(mycursor.rowcount, "The Results : ")
