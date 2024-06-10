import sqlite3
import json
import os
import sys
import pandas as pd

class Sqlitect22:

  def __init__(self,param_json):

     # Get the param file
     with open(param_json) as f:
          self.param_data = json.load(f)

     # Access to ElasticSearch local
     self.path = self.param_data["path"]
     self.pathlength = len(self.path)
     self.pathProcessed = self.param_data["pathProcessed"]
     # --- Data Files
     self.stapcsv = self.param_data["stapcsv"]
     self.collcsv = self.param_data["collcsv"]
     self.dbuserscsv = self.param_data["dbuserscsv"]
     self.seltypcsv = self.param_data["seltypcsv"]
     self.nodescsv = self.param_data["nodescsv"]
     self.seltypcsv = self.param_data["seltypcsv"]
     self.guardecscsv = self.param_data["ecsct22"]
     self.sqlstowatchcsv = self.param_data["ecsct22"]

     # --- Required Keys
     self.collHost = self.param_data["HostnameColl"]
     self.collIP = self.param_data["IPColl"]
     self.stapHost = self.param_data["HostnameStap"]
     self.dbuser = self.param_data["DBUser"]
     self.seltyp = self.param_data["seltyp"]
     self.node = self.param_data["Node"]
     self.stapIP = self.param_data["IPStap"]
     self.guardecs = "guardium"
     self.sqlstowatch = "hsh"

     # --- Extractions and Preds 
     self.sqlite = self.param_data["sqlite"]
     self.predscsv = self.param_data["predscsv"]
     self.uwatchsqlscsv = self.param_data["uwatchsqlscsv"]
     self.sqlstowatchcsv = self.param_data["sqlstowatchcsv"]
     # self.extractscsv = self.param_data["extractscsv"]


     # --- SQLite
     self.sqlite = self.param_data["sqlite"]

  def sqlstowatchTable(self):
     # ---- Reading of Metadata files
     # datafile_colls = self.path + self.collcsv
     datafile_sqlstowatch =  self.sqlstowatchcsv
     # --- Guardecs
     # breakpoint()
     df_sqlstowatch = pd.read_csv(datafile_sqlstowatch, quotechar="'")
     print (df_sqlstowatch.columns.values.tolist())
     sqlstowatch = df_sqlstowatch.get(self.guardecs)

     non_null_row_count = df_sqlstowatch[self.sqlstowatch].count()
     row_count = len(df_sqlstowatch[self.sqlstowatch])
     unique_row_count = df_sqlstowatch[self.sqlstowatch].nunique()
     if non_null_row_count != row_count or row_count != unique_row_count :
         print ('Guardium sqlstowatch  Metadata not consistent - Pls correct : ' , datafile_sqlstowatch , ' and run again ')
         print ( non_null_row_count, row_count, unique_row_count )
         exit(0)

     df_sqlstowatch.to_sql('sqlstowatch', self.conn, if_exists='replace', index=False)
     self.conn.commit()
     self.cursor.execute('SELECT * FROM sqlstowatch LIMIT 500')
     data = self.cursor.fetchall()
     return (data)



  def guardecsTable(self):
     # ---- Reading of Metadata files
     # datafile_colls = self.path + self.collcsv
     datafile_guardecs =  self.guardecscsv
     # --- Guardecs
     # breakpoint()
     df_guardecs = pd.read_csv(datafile_guardecs, quotechar="'")
     print (df_guardecs.columns.values.tolist())
     guardecs = df_guardecs.get(self.guardecs)

     non_null_row_count = df_guardecs[self.guardecs].count()
     row_count = len(df_guardecs[self.guardecs])
     unique_row_count = df_guardecs[self.guardecs].nunique()
     if non_null_row_count != row_count or row_count != unique_row_count :
         print ('Guardium ecs mapping  Metadata not consistent - Pls correct : ' , datafile_guardecs , ' and run again ')
         print ( non_null_row_count, row_count, unique_row_count )
         exit(0)

     df_guardecs.to_sql('guardecs', self.conn, if_exists='replace', index=False)
     self.conn.commit()
     self.cursor.execute('SELECT * FROM guardecs LIMIT 500')
     data = self.cursor.fetchall()
     return (data)

  def seltypTable(self):
     # ---- Reading of Metadata files
     datafile_seltyp =  self.seltypcsv
     # --- Guardecs
     # breakpoint()
     df_seltyp = pd.read_csv(datafile_seltyp, quotechar="'")
     print (df_seltyp.columns.values.tolist())
     seltyp = df_seltyp.get(self.seltyp)

     non_null_row_count = df_seltyp[self.seltyp].count()
     row_count = len(df_seltyp[self.seltyp])
     unique_row_count = df_seltyp[self.seltyp].nunique()
     if non_null_row_count != row_count or row_count != unique_row_count :
         print ('Guardium ecs mapping  Metadata not consistent - Pls correct : ' , datafile_seltyp , ' and run again ')
         print ( non_null_row_count, row_count, unique_row_count )
         exit(0)

     df_seltyp.to_sql('seltyp', self.conn, if_exists='replace', index=False)
     self.conn.commit()
     self.cursor.execute('SELECT * FROM seltyp LIMIT 500')
     data = self.cursor.fetchall()
     return (data)

  def stapsTable(self):
     # ---- Reading of Metadata files
     # datafile_staps = self.path + self.stapcsv
     datafile_staps = self.stapcsv
     # datafile_colls = self.path + self.collcsv

     # --- STAPs
     df_staps = pd.read_csv(datafile_staps, quotechar="'")
     print (df_staps.columns.values.tolist())

     stapHost = df_staps.get(self.stapHost)
     if stapHost is None:
         print(self.stapHost , ' column Does NOT exist in ', self.stapcsv,' Please correct in param-data.json')
         exit(0)
     stapIP = df_staps.get(self.stapIP)
     if stapIP is None:
         print(self.stapIP , ' column Does NOT exist in ', self.stapcsv,' Please correct in param-data.json')
         exit(0)

     non_null_row_count = df_staps[self.stapHost].count()
     row_count = len(df_staps[self.stapHost])
     unique_row_count = df_staps[self.stapHost].nunique()
     if non_null_row_count != row_count or row_count != unique_row_count :
         print ('Staps Metadata not consistent - Pls correct : ' , datafile_staps , ' and run again ')
         print ( non_null_row_count, row_count, unique_row_count )
         exit(0)
     df_staps.to_sql('staps', self.conn, if_exists='replace', index=False)
     self.conn.commit()
     self.cursor.execute('SELECT * FROM staps LIMIT 1000')
     data = self.cursor.fetchall()
     # print (data)
     return (data)

  def collsTable(self):
     # ---- Reading of Metadata files
     # datafile_colls = self.path + self.collcsv
     datafile_colls =  self.collcsv
     # --- Colls
     df_colls = pd.read_csv(datafile_colls, quotechar="'")
     print (df_colls.columns.values.tolist())
     collHost = df_colls.get(self.collHost)
     collIP = df_colls.get(self.collIP)
     if collIP is None:
         print(self.collIP , ' column Does NOT exist in ', self.collcsv,' Please correct in param-data.json')
         exit(0)
     non_null_row_count = df_colls[self.collHost].count()
     row_count = len(df_colls[self.collHost])
     unique_row_count = df_colls[self.collHost].nunique()
     if non_null_row_count != row_count or row_count != unique_row_count :
         print ('Collectors Metadata not consistent - Pls correct : ' , datafile_colls , ' and run again ')
         print ( non_null_row_count, row_count, unique_row_count )
         exit(0)

     df_colls.to_sql('colls', self.conn, if_exists='replace', index=False)
     self.conn.commit()
     self.cursor.execute('SELECT * FROM colls LIMIT 100')
     data = self.cursor.fetchall()
     # print (data)
     return (data)

  def dbusersTable(self):
     # ---- Reading of Metadata files
     # datafile_colls = self.path + self.collcsv
     datafile_dbusers =  self.dbuserscsv
     # --- DBUsers
     df_dbusers = pd.read_csv(datafile_dbusers, quotechar="'")
     print (df_dbusers.columns.values.tolist())
     DBUser = df_dbusers.get(self.dbuser)
     # --- Checking that the mandatory column, as described in the param_data.json file exists
     if DBUser is None:
         print(self.dbuser , ' column Does NOT exist in ', self.dbuserscsv,' Please correct in param-data.json')
         exit(0)

     non_null_row_count = df_dbusers[self.dbuser].count()
     row_count = len(df_dbusers[self.dbuser])
     unique_row_count = df_dbusers[self.dbuser].nunique()
     if non_null_row_count != row_count or row_count != unique_row_count :
         print ('DB Users Metadata not consistent - Pls correct : ' , datafile_dbusers , ' and run again ')
         print ( non_null_row_count, row_count, unique_row_count )
         exit(0)

     elif data == 'seltyp' :
             data = self.seltypTable()
     df_dbusers.to_sql('dbusers', self.conn, if_exists='replace', index=False)
     self.conn.commit()
     self.cursor.execute('SELECT * FROM dbusers LIMIT 500')
     data = self.cursor.fetchall()
     return (data)

  def nodesTable(self):
     # ---- Reading of Metadata files
     # datafile_colls = self.path + self.collcsv
     datafile_nodes =  self.nodescsv
     # --- DBUsers
     df_nodes = pd.read_csv(datafile_nodes, quotechar="'")
     print (df_nodes.columns.values.tolist())
     node = df_nodes.get(self.node)
     if node is None:
         print(self.node , ' column Does NOT exist in ', self.nodescsv,' Please correct in param_data.json')
         exit(0)
     non_null_row_count = df_nodes[self.node].count()
     row_count = len(df_nodes[self.node])
     unique_row_count = df_nodes[self.node].nunique()
     if non_null_row_count != row_count or row_count != unique_row_count :
         print ('DB Users Metadata not consistent - Pls correct : ' , datafile_nodes , ' and run again ')
         print ( non_null_row_count, row_count, unique_row_count )
         exit(0)

     df_nodes.to_sql('nodes', self.conn, if_exists='replace', index=False)
     self.conn.commit()
     self.cursor.execute('SELECT * FROM nodes LIMIT 1500')
     data = self.cursor.fetchall()
     return (data)

  # -- Predictions -----
  def predsTable(self):
     # ---- Reading of Preds files --- No Checks on the Data --- 
     # ---- Here only to initiate the table with initial csv file
     datafile_preds =  self.predscsv
     # --- Preds
     df_preds = pd.read_csv(datafile_preds, quotechar="'")
     print (df_preds.columns.values.tolist())

     df_preds.to_sql('preds', self.conn, if_exists='replace', index=False)
     self.conn.commit()
     self.cursor.execute('SELECT * FROM preds LIMIT 1500')
     data = self.cursor.fetchall()
     return (data)

  # --  Extractions -----
  def extractsTable(self):
     # ---- Reading of extractcounters files --- No Checks on the Data --- 
     # ---- Here only to initiate the table with initial csv file
     datafile_extracts =  self.extractscsv
     # --- Extractcounters
     df_extracts = pd.read_csv(datafile_extracts, quotechar="'")
     print (df_extracts.columns.values.tolist())

     df_extracts.to_sql('extracts', self.conn, if_exists='replace', index=False)
     self.conn.commit()
     self.cursor.execute('SELECT * FROM extracts LIMIT 1500')
     data = self.cursor.fetchall()
     return (data)     


  # -- sqlswatch SQLs  under watch  -----
  def uwatchsqlsTable(self):
     # ---- Reading of extractcounters files --- No Checks on the Data --- 
     # ---- Here only to initiate the table with initial csv file
     datafile_uwatchsqls =  self.uwatchsqlscsv
     # --- Under Watch SQLs
     df_uwatchsqls = pd.read_csv(datafile_uwatchsqls, quotechar="'")
     print (df_uwatchsqls.columns.values.tolist())

     df_uwatchsqls.to_sql('uwatchsqls', self.conn, if_exists='replace', index=False)
     self.conn.commit()
     self.cursor.execute('SELECT * FROM uwatchsqls LIMIT 1500')
     data = self.cursor.fetchall()
     return (data)


  def openSqlite(self) :
     #self.conn = sqlite3.connect('sqlite/sqlitect22')
     self.conn = sqlite3.connect(self.sqlite)

     self.cursor = self.conn.cursor()

     return()

     # Create table
     # c.execute('''create table stocks (date text, trans text, symbol text, qty real, price real)''')
     # Insert a row of data
     # c.execute("""insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)""")
     # Save (commit) the changes
     # conn.commit()
     # We can also close the cursor if we are done with it

  def closeSqlite(self):
     self.cursor.close()
     return()


   # --- The mainProcess 
  def mainProcess(self,data):
     self.openSqlite()
    
     if data == 'staps' :
             data = self.stapsTable()
     elif data == 'colls' :
             data = self.collsTable()
     elif data == 'dbusers' :
             data = self.dbusersTable()
     elif data == 'nodes' :
             data = self.nodesTable()
     elif data == 'preds' :
             data = self.predsTable()
     elif data == 'uwatchsqls' :
             data = self.uwatchsqlsTable()
     elif data == 'extracts' :
             data = self.extractsTable()
     elif data == 'guardecs' :
             data = self.guardecsTable()
     elif data == 'seltyp' :
             data = self.seltypTable()
     elif data == 'sqlstowatch' :
             data = self.sqlstowatchTable()
     else:
             print( "No data to be uploaded selected - nothing was done - ")

     self.closeSqlite()

     return(data)
