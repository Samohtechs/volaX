#! /usr/bin/python3

########################################
# WRITTEN BY: SAMOH @ghostshado3       #
########################################

from volaX import help
from volaX import volatility
import history

# main driver code
if __name__ == "__main__":
  print("""
  ***   *** ******** ****         ****            ****   ****
  ***   *** ******** ****      ***    ***          **** ****
  ***   *** ***  *** ****      ***    ***           ******
  ***   *** ***  *** ****      **********           ******
  ***   *** ***  *** ****      **********         **** ****
   *** ***  ******** ********* ***    ***        ****   ****
    ****    ******** ********* ***    ***       ****     **** v1.0
  
  Memory Forensics made Easy!""")

  print("""  ########################################################################################################
  # PLEASE NOTE: THIS IS NOT A NEW IMPLEMENTATION OF VOLATILITY. IT SIMPLY USES THE VERSION OF VOLATILITY#
  # (specifically volatility 2). This simple program aims to simply ease the use of volatility. It saves #
  # the profile of the image all you have to do is focus on other commands to accomplish your task. To   #
  # To change profile use cp or cprofile, a prompt will follow for you to enter another profile.         #
  ########################################################################################################

  ########################################################################################################
  # WRITTEN BY: SAMOH MOHAMMED. TWITTER @ghostshado3. GITHUB @samohtechs. Website: https://samohtechs.tk #
  # you can clone or fork this work here https://github.com/Samohtechs/volaX                             #
  ########################################################################################################""")

  history.HistoryConsole()
  help()

  print("Select volatility version. Must be enabled globally.\n1 - To specify your own path (If you wish this path to be persistent, open volpath.py and add your path to the path_variable and version to vol_version veriable. and next time enter 1.)\n2 - Volatility 2 (Must be accessible as volatility)\n3 - Volatility 3 (Must be accessible as volatility3).\n4 - To use your own path as specified in path_variable in volpath.py\n0 - Exit")
  response = str(input("Volatility:> "))
  while(True):
    try:
      if(response == "0"):
        break
      elif(response == "1"):
        from os import path
        try:
          mypath = str(input("Enter full path: "))
          myversion = int(input("Enter version: "))
          if(mypath == "" or mypath == " " or myversion == "" or myversion == " "):
            print("Path and/or Version cannot be blank")
          else:
            volatility(mypath, str(myversion), mypath)
        except ValueError:
          print("version should be of type integer")
        except:
          exit()
      elif(response == "2"):
        volatility("volatility")
      elif(response == "3"):
        volatility("volatility3", "3")
      elif(response == "4"):
        import volpath
        try:
          mypath = str(volpath.path_variable)
          myversion = int(volpath.vol_version)
          if(mypath == "" or mypath == " " or myversion == "" or myversion == " "):
            print("Path and/or Version cannot be blank. Please set required variables in volpath.py")
            break
          else:
            volatility(mypath, str(myversion), mypath)
        except ValueError:
          print("version should be of type integer")
        except:
          exit()
      else:
        print("ERROR: You did not select from specified options.")
        break
    except:
      exit()
  exit()
    
