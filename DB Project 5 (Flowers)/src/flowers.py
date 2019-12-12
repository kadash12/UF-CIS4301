import sqlite3
connection = sqlite3.connect('flowers2019.db')
cursor = connection.cursor()

s = ""
while(s != "end"):
    s = input("Select one: query, update, insert, end \n")
    if s == "query":
        s = input("Input a flower to show recent sightings \n")
        cursor.execute(
        '''SELECT *
        FROM SIGHTINGS
        where name = "'''+ s + '''"
        ORDER BY sighted DESC
        LIMIT 10''')
        row = cursor.fetchone()
        while row is not None:
            print(str(row))
            row = cursor.fetchone()
        connection.commit()
    elif s == "update":
        s = input("Update one: \n")
        newGenus =""
        newSpecies=""
        newComname=""
        if s == "one":
            oldComname = "\'"+input("Input the comname of the flower to update: \n")+"\'"
            s = input("What variables would you like to change?: \n")
            count = 0
            if "genus" in s:
                count = count+1
            if "species" in s:
                count = count+1

            if "genus" in s:
                newGenus = "genus = \'"+ input("Input the new genus: \n") +"\'"
                count = count -1
                if count != 0:
                    newGenus += ", "
            if "species" in s:
                newSpecies = "species = \'"+ input("Input the new species: \n") +"\'"
                count = count -1
                if count != 0:
                    newSpecies += ", "
            if "comname" in s:
                newComname = "comname = \'"+ input("Input the new comname: \n") +"\'"
            strCommand = '''UPDATE FLOWERS
            SET '''+newGenus+newSpecies+newComname+ " WHERE comname = "+ oldComname;

            cursor.execute(strCommand)
            row = cursor.fetchone()
            while row is not None:
                print(str(row))
                row = cursor.fetchone()
            connection.commit()

    elif s == "insert":
        newComname = "\""+input("Input the comname: \n")+"\", "
        newPerson = "\""+input("Input the person: \n")+"\", "
        newLocation = "\""+input("Input the location: \n")+"\", "
        newSighted = "\""+input("Input when sighted: \n")+"\" "
    
        cursor.execute(
        "INSERT INTO SIGHTINGS VALUES "+"("+newComname+newPerson+newLocation+newSighted+")")
        row = cursor.fetchone()
        while row is not None:
            print(str(row))
            row = cursor.fetchone()
        connection.commit()
