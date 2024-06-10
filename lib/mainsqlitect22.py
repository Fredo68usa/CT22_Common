from sqlitect22 import Sqlitect22
import sys
import sqliteread



if __name__ == '__main__':
      print("Start Management of Metadata, Staps and Collectors")
      readWrite = input("read or write ? ")
      # readWrite  = str(sys.argv[1])
      print("staps, colls, dbusers, nodes, preds, uwatchsqls, extracts, guardecs, seltyp, sqlswatch")
      data = input("What table ?")
      # data  = str(sys.argv[2])
      # print ('Type of myListIPs', type(myListIPs))
      # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP

      if readWrite == "read" :
         p2 = sqliteread.sqliteread("param_data.json")
         print("Start Reading of Metadata, Staps and Collectors")
         data = p2.mainProcess(data)
         print (data)
      elif readWrite == "write":
         p1 = Sqlitect22("param_data.json")
         print("Start Writing of Metadata, Staps and Collectors")
         data = p1.mainProcess(data)
         print (data)
      else :
         print ("param1 = read or write , param2 = table")
         print ("Do it again ...")

