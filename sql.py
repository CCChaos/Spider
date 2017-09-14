#encoding=utf-8
import mysql.connector as MySqlConnect

def SQLExecute(sql):
    ret = True
    errinfo = ""
    try:
        conn = MySqlConnect.connect(user='spider', password='spider', host='123.56.134.184', db='spider')
        cursor = conn.cursor()
        cursor.execute(sql)
        rc = cursor.rowcount
        conn.commit()
        conn.close()
    except Exception as e:
        errinfo = 'Database Error for myql: \n\t %s' % (sql)
        ret = False
    finally:
        if errinfo != "":
            print errinfo
        return ret

def SQLCreateTable(housedict, table_name):
    table_dict = ""
    for key in housedict.iterkeys():
        if key == 'id':
            continue
        if table_dict == '':
            table_dict = "%s varchar(128)" % key
        else:
            table_dict = "%s,%s varchar(128)" % (table_dict, key)
    sql = "CREATE TABLE %s ( id varchar(32) primary key, %s )ENGINE=InnoDB DEFAULT CHARSET utf8 COLLATE utf8_general_ci;" % (table_name, table_dict)
    return SQLExecute(sql)

def SQLInsertHouse(housedict, table_name):
    table_value = ""
    for (k, v) in housedict.iteritems():
        if table_value == '':
            table_value = "%s = \"%s\"" % (k,v)
        else:
            table_value = "%s, %s = \"%s\"" % (table_value, k, v)
    sql = "INSERT INTO %s set %s;" % (table_name, table_value)
    return SQLExecute(sql)
