import pypyodbc


def Attr():
    connstring = "Driver={SQL Server};Server=bi-serv;Database=RetinaCSDatabase;  Uid=Administrator;"
    try:
        print("connecting to database...")

        sqlconn = pypyodbc.connect(connstring)
        print("database connection successful!")

    except Exception as e:
        print(e.args)














Attr()