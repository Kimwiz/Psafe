import urllib.request
import pypyodbc
import urllib.response
import csv


class PSafe:

    def __init__(self):
        pass

        #self.connection()


    def connection(self):
        try:
            headers = {"Authorization":"PS-Auth key=6AFD65B3-8249-4DE7-BD6A-560E46AA02BC; runas:mdavis;"}

            url = "https://btu-bi/eEye.RetinaCS.Server/api/public/v3/"
            conn = urllib.request.Request(url, headers)


            print("connection to {} successful!".format(conn.data))
        except:
            print("connection to {} failed".format(url))


    def db_version(self):
        connstring = 'Driver={SQL Server};Server=BI-SERV;Database=RetinaCSDatabase;Uid=sa;Pwd=btlab16*;'
        try:
            print("connecting to database...")

            sqlconn = pypyodbc.connect(connstring)
            print("database connection successful!")

        except:
            print("couldn't connect to database")

        SQLCOMM = "SELECT [DBVersion] FROM [RetinaCSDatabase].[dbo].[Version]"

        try:
            cursor = sqlconn.cursor()
            query = cursor.execute(SQLCOMM)
            print('Database Version:{}'.format(query.fetchall()))
        except:
            print("COULDNT EXECUTE SQL COMMAND!!!")


    def user_groups(self):
        connstring = 'Driver={SQL Server};Server=BTU-BI;Database=RetinaCSDatabase;Uid=sa;Pwd=btlab16*;'
        try:
            print("connecting to database...")

            sqlconn1 = pypyodbc.connect(connstring)
            print("database connection successful!")
        except:
            print("couldn't connect to database")

        SQLCOMM = "select * from RetinaCSDatabase.dbo.UserGroup"

        try:
            cursor=sqlconn1.cursor()
            query = cursor.execute(SQLCOMM)
            #print('Usergroups:{}'.format(query.fetchall()))
            for row in query.fetchall():
                print (row)
        except:
            print("COULDNT EXECUTE {}!!!".format(query))


    def usergroups_by_id(self):


        connstring = 'Driver={SQL Server};Server=BTU-BI;Database=RetinaCSDatabase;Uid=sa;Pwd=btlab16*;'
        try:
            print("connecting to database...")

            sqlconn1 = pypyodbc.connect(connstring)
            print("database connection successful!")

        except:
            print("couldn't connect to database")

        SQLCOMM = "select GroupID from RetinaCSDatabase.dbo.UserGroup "

        try:
            cursor = sqlconn1.cursor()
            query = cursor.execute(SQLCOMM)
           # exfile=open('table.cv','w')
            #datawriter=csv.writer(exfile)


            # print('Usergroups:{}'.format(query.fetchall()))
            for row in query.fetchall():
                print(row)

        except:
            print("COULDNT EXECUTE {}!!!".format(query))



    def UserG_by_name(self):

        connstring = 'Driver={SQL Server};Server=BTU-BI;Database=RetinaCSDatabase;Uid=sa;Pwd=btlab16*;'
        try:
            print("connecting to database...")

            sqlconn1 = pypyodbc.connect(connstring)
            print("database connection to {} successful!")


        except:
            print("couldn't connect to database")

        SQLCOMM = "select Name from RetinaCSDatabase.dbo.UserGroup "

        try:
            cursor = sqlconn1.cursor()
            query = cursor.execute(SQLCOMM)
            # print('Usergroups:{}'.format(query.fetchall()))
            for row in query.fetchall():
                print(row)
        except:
            print("COULDNT EXECUTE {}!!!".format(query))



    def UG_w_Perm(self):
        connstring = 'Driver={SQL Server};Server=BTU-BI;Database=RetinaCSDatabase;Uid=sa;Pwd=btlab16*;'
        try:
            print("connecting to database...")

            sqlconn1 = pypyodbc.connect(connstring)
            print("database connection successful!")

        except:
            print("couldn't connect to database")

        SQLCOMM = """
                  Update RetinaCSDatabase.dbo.UserGroup_SmartRule
                  set Permission=0 where GroupID=2 AND SmartRuleID=2002
                  """

        try:
            cursor = sqlconn1.cursor()
            query = cursor.execute(SQLCOMM)
            # print('Usergroups:{}'.format(query.fetchall()))
            print("Permission changed successfully")
           # print(query.fetchall())
        except:
            print("COULDNT EXECUTE {}!!!".format(query))



    def users_by_GID(self,id):


        connstring = 'Driver={SQL Server};Server=BTU-BI;Database=RetinaCSDatabase;Uid=sa;Pwd=btlab16*;'
        try:
            print("connecting to database...")

            sqlconn1 = pypyodbc.connect(connstring)
            print("database connection successful!")

        except:
            print("couldn't connect to database")

        #SQLCOMM = "select * from RetinaCSDatabase.dbo.UserGroup where GroupID=? ",id

        try:
            cursor = sqlconn1.cursor()
            query = cursor.execute("""select * from RetinaCSDatabase.dbo.UserGroup where GroupID=? """,[id])
            # print('Usergroups:{}'.format(query.fetchall()))
            for row in query.fetchall():

                print(row)
        except:
            print("COULDNT EXECUTE {}!!!".format(query))


    def Workgps(self):

        connstring = 'Driver={SQL Server};Server=BI-SERV;Database=RetinaCSDatabase;Uid=BI-SERV/Administrator;Pwd=btlab16*;'
        try:
            print("connecting to database...")
            query=""
            sqlconn1=""
            sqlconn1 = pypyodbc.connect(connstring)
            print("database connection successful!")

        except Exception as e:
            print(e.args)

        SQLCOMM = "Select * From RetinaCSDatabase.dbo.WorkGroup "

        try:
            cursor = sqlconn1.cursor()
            query = cursor.execute(SQLCOMM)
            # print('Usergroups:{}'.format(query.fetchall()))
            rows=query.fetchall()


            for row in rows:
               print (row)


        except:
            print("COULDNT EXECUTE {}!!!".format(query))








xobj=PSafe()

xobj.Workgps()








