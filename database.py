import oracledb;

def connect_to_db():
    # Путь к файлу instantclient_23_5 (поменять)
    dir = r"C:\Users\444\Documents\instantclient_23_5";
        #  устанавливаем режим thick 
    oracledb.init_oracle_client(lib_dir=dir);
    try:
        # пытаемся подключиться к базе данных (поменять)
        con = oracledb.connect(user="koksfox", password="1024", host="192.168.56.1", port=1521, service_name="XEPDB1");
        # Create a cursor
        cursor = con.cursor()
        # Execute a SELECT statement
        cursor.execute('SELECT 1 FROM dual')
        # Fetch the results
        results = cursor.fetchall()
        str_results = ' '.join(map(str, results))
        # Loop through the results
        return str_results
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        return('Can`t establish connection to database Oracle');