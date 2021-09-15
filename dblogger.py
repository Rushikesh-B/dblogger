#!/usr/bin/python
import sys
import re

arg = sys.argv

filename = ""
transactionId = ""

if "-h" in arg:
    if len(arg) > 2:
        print("Not valid argument")
        print("try other options from help")
        sys.exit()
    else:
          print ('-f <input-filename>')
          print ('-l <list all unique transaction ids: every log has a field trid >')
          print ('-t <list all log lines for the given transaction-id >')
          print ('-c <list all complete requests: check for msg: Start processing request & Finished processing request >')
          sys.exit()


if "-f" in arg:
     i = arg.index("-f")

     if i == (len(arg) - 1):
         print("No file name provided")
         sys.exit();
     else:
         if arg[i+1].endswith(".log"):
            filename = arg[i+1]
         else:
             print("Please provide a .log file")
             sys.exit()


if "-l" in arg:
    trid = []

    if(filename==""):
      print("No filename provided")
      sys.exit()

    f = open(filename, "r")
    line_regex = re.compile("trid=\d+")
    for line in f:
     match = line_regex.findall(line)
     if(match):
      temp = match[0]
      temp = temp.replace("trid=","")
      trid.append(temp)

    final_trid = list(dict.fromkeys(trid))

    for t in final_trid:
        print(t.strip("\'"))


if "-c" in arg:

    if(filename==""):
      print("No filename provided")
      sys.exit()

    f = open(filename, "r")

    for line in f:
     if("Start processing request;" in line or "Finished processing request;" in line):
        print(line)


if "-t" in arg:

    if(filename==""):
      print("No filename provided")
      sys.exit()

    i = arg.index("-t")

    if i == (len(arg) - 1):
        print("No transaction ID provided")
        sys.exit();
    else:
        if arg[i+1].isdigit():
           transactionId = arg[i+1]
           f = open(filename, "r")

           for line in f:
            if(transactionId in line):
               print(line)
        else:
            print("Transaction ID not found")
