import pyodbc


def init_db(server_name, database_name):
    conn = pyodbc.connect(
        'Driver={SQL Server};' 'Server=' + server_name + ';' 'Database=' + database_name + ';'  'Trusted_Connection=yes;')

    return conn.cursor()


def execute_query(query, commit):
    res = []
    try:
        # OPENED CONNECTION TO DB
        cursor = init_db('DESKTOP-LFCINUN', 'utc503_project')
        try:
            # RAN QUERY
            cursor.execute(query)
        except:
            # QUERY FAILED
            raise
        else:
            if commit:
                cursor.commit()
                res.append('success')
            else:
                for row in cursor:
                    res.append(row)
        finally:
            # CLOSED CONNECTION TO DB
            cursor.close()

    except Exception as e:
        print('Something went wrong:' + str(e))

    return res
