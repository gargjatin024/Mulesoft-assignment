# Mulesoft-assignment
Working with Database

#!/usr/bin/python

import sqlite3
con=sqlite3.connect('movies.db') 
cur = con.cursor()
#creation of table
cur.execute("CREATE TABLE MOVIE(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,ACTOR TEXT NOT NULL,ACTRESS TEXT NOT NULL,DIRECTOR TEXT NOT NULL,YEAR OF RELEASE TEXT NOT NULL)");
#con.commit();


#Inserting of data into table
cur.execute('INSERT INTO TABLE(ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR OF RELEASE)'
	     'VALUES (1,"Pushpa","Allu Arjun","Rashmika Mandanna","Sukumar",2022)');
cur.execute('INSERT INTO TABLE(ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR OF RELEASE)'
	    ' VALUES (2,"Baahubali","Prabhas","Anushka Shetty","S.S.RajaMouli",2015)');
cur.execute('INSERT INTO TABLE(ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR OF RELEASE)'
	     'VALUES (3,"Radhe Shyam","Prabhas","Pooja Hegde","Radhe Krishna Kumar",2022)');
cur.execute('INSERT INTO TABLE(ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR OF RELEASE)'
	    ' VALUES (4,"KGF 2","Yash","Srinidhi Shetty","Prashanth Neel",2022)');
cur.execute('INSERT INTO TABLE(ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR OF RELEASE)'
	    ' VALUES (5,"RRR","N.T.Rama Rao jr.","Alia Bhatt","S.S.RajaMouli",2022)');
con.commit();


#Query using Select Statement
#Retrieve all Rows from Table
cursor=cur.execute('SELECT * FROM MOVIE');
for row in cursor:
	print "ID=",row[0]
	print "NAME=",row[1]
	print "ACTOR=",row[2]
  print "ACTRESS=",row[3]
  print "DIRECTOR=",row[4],"\n"
	print "YEAR OF RELEASE=",row[5],"\n"
#Retrieve movies based from actor's name
cursor=cur.execute('SELECT * FROM MOVIE WHERE ACTOR="Prabhas"');
for row in cursor:
	print "ID=",row[0]
	print "NAME=",row[1]
	print "ACTOR=",row[2]
  print "ACTRESS=",row[3]
  print "DIRECTOR=",row[4],"\n"
	print "YEAR OF RELEASE=",row[5],"\n"
con.close();
