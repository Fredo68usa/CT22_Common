import sqlite3
import json
import os
import sys
import pandas as pd

class sqliteread :

  def __init__(self,param_json):

     # Get the param file
     with open(param_json) as f:
          self.param_data = json.load(f)

     # print (self.param_data)

     # Access to ElasticSearch local
     self.path = self.param_data["path"]
     self.pathlength = len(self.path)
     self.pathProcessed = self.param_data["pathProcessed"]
     # --- Data Files
     self.stapcsv = self.param_data["stapcsv"]
     self.collcsv = self.param_data["collcsv"]
     self.dbuserscsv = self.param_data["dbuserscsv"]
     self.nodescsv = self.param_data["nodescsv"]
     self.seltypcsv = self.param_data["seltypcsv"]

     # --- Required Keys
     self.collHost = self.param_data["HostnameColl"]
     self.collIP = self.param_data["IPColl"]
     self.stapHost = self.param_data["HostnameStap"]
     self.dbuser = self.param_data["DBUser"]
     self.node = self.param_data["Node"]
     self.stapIP = self.param_data["IPStap"]

     # --- Extractions and Preds 
     self.sqlite = self.param_data["sqlite"]
     self.predscsv = self.param_data["predscsv"]
     self.uwatchsqlscsv = self.param_data["uwatchsqlscsv"]
     # self.extractscsv = self.param_data["extractscsv"]


     # --- SQLite
     self.sqlite = self.param_data["sqlite"]

  def readstapsTable(self):
     self.cursor.execute('SELECT * FROM staps LIMIT 1000')
     data = self.cursor.fetchall()
     # print (data)
     return (data)

  def readguardecsTable(self):
     self.cursor.execute('SELECT * FROM guardecs LIMIT 1000')
     data = self.cursor.fetchall()
     column_names = [description[0] for description in self.cursor.description]
     df_guardecs = pd.DataFrame(data, columns=column_names)
     print (df_guardecs)
     return (data)

  def readcollsTable(self):
     self.cursor.execute('SELECT * FROM colls LIMIT 100')
     data = self.cursor.fetchall()
     # print (data)
     return (data)

  def readdbusersTable(self):
     self.cursor.execute('SELECT * FROM dbusers LIMIT 500')
     data = self.cursor.fetchall()
     return (data)

  def readnodesTable(self):
     self.cursor.execute('SELECT * FROM nodes LIMIT 1500')
     data = self.cursor.fetchall()
     column_names = [description[0] for description in self.cursor.description]
     df_nodes = pd.DataFrame(data, columns=column_names)
     return (df_nodes)

  # -- Predictions -----
  def readpredsTable(self):
     self.cursor.execute('SELECT * FROM preds LIMIT 1500')
     data = self.cursor.fetchall()
     column_names = [description[0] for description in self.cursor.description]
     df_preds = pd.DataFrame(data, columns=column_names)
     return (df_preds)

  # --  Extractions -----
  def readextractsTable(self):
     self.cursor.execute('SELECT * FROM extracts LIMIT 1500')
     data = self.cursor.fetchall()
     column_names = [description[0] for description in self.cursor.description]
     df_extracts = pd.DataFrame(data, columns=column_names)
     return (df_extracts)

  # --  SQLs  under watch  -----
  def readuwatchsqlsTable(self):
     self.cursor.execute('SELECT * FROM uwatchsqls LIMIT 1500')
     data = self.cursor.fetchall()
     return (data)


  def openSqlite(self) :
     #self.conn = sqlite3.connect('sqlite/sqlitect22')
     self.conn = sqlite3.connect(self.sqlite)

     self.cursor = self.conn.cursor()

     return()

  def closeSqlite(self):
     self.cursor.close()

     return()


   # --- The mainProcess 
  def mainProcess(self,data):
     self.openSqlite()
    
     if data == 'staps' :
             data = self.readstapsTable()
     elif data == 'colls' :
             data = self.readcollsTable()
     elif data == 'dbusers' :
             data = self.readdbusersTable()
     elif data == 'nodes' :
             data = self.readnodesTable()
     elif data == 'preds' :
             data = self.readpredsTable()
     elif data == 'uwatchsqls' :
             data = self.readuwatchsqlsTable()
     elif data == 'extracts' :
             data = self.readextractsTable()
     elif data == 'guardecs' :
             data = self.readguardecsTable()
     else:
             print( "No data  selected - nothing was done - ")

     self.closeSqlite()

     return(data)
