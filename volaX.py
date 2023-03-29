#! /usr/bin/python3

####################################################################################################################
# PLEASE NOTE: THIS IS NOT A NEW IMPLEMENTATION OF VOLATILITY. IT SIMPLY USES THE VERSION OF VOLATILITY            #
# (specifically volatility 2). This simple program aims to simply ease the use of volatility.                      #
# It saves the imageName of the image all you have to do is focus on other commands to accomplish your task.         #
# To change imageName use cp or cimageName, a prompt will follow for you to enter another imageName.                     #
####################################################################################################################

####################################################################################################################
# WRITTEN BY: SAMOH MOHAMMED. TWITTER @ghostshado3. GITHUB @samohtechs                                             #
# you can clone or fork this work here www.twitter.com/samohtechs/volaX                                            #
####################################################################################################################

import os

def help():
        print("Welcome To Volatility!")
        print("USAGE:")
        print("help           this help")
        print("cp, cimageName   change imageName name (when imageName has already been selected)")
        print("q, exit, quit  exit program and return to shell")
        print("shell          to enter shell commands mode")
        print("")

def volatility(volatility, version="2"):
    while(True):
        try:
            ## Read image or Image Name...
            imageName = input(">> Enter name of image: ")

            if(imageName == "q" or imageName == "exit" or imageName == "quit"):
                print("Goodbye...")
                exit()
            elif(imageName == "help"):
                help()
                continue
            elif(imageName == "cp" or imageName == "cimageName"):
                print("INFO: Cannot change profile. No profile has been used yet.")
                continue
            elif(imageName == "" or imageName == " "):
                print("ALERT: File name not supplied...")
                continue
            else:
                if(version == "2"):
                    if(os.system(volatility+" -f " + imageName + " imageinfo") != 0):
                        continue
                    break
                else:
                    if(os.system(volatility+" -f "+ imageName + " windows.info") != 0):
                        continue
                    break
        except FileNotFoundError:
            print("ERROR: File Not Found...")
            continue
        except KeyboardInterrupt:
            print("KeyboardInterrupt: To exit type q, exit or quit")
            continue
    
    # Check if version is volatility3 and set None to profile name
    if(version == "3"):
        profile_name = "P:None"
    else:
        ## profile name to be used...
        profile_name = input("\n>> Enter profile name to use: ")

    while(True):
        try:
            if(profile_name == "" or profile_name == " "):
                print("ALERT: Please provide a profile name...")
                profile_name = input(">> Enter profile name to use: ")
                continue
            else:
                if(version == "3"):
                    print("\n(volatility -f "+imageName+")")
                else:
                    print("\n(volatility -f "+imageName+" --profile="+profile_name+")")

                user_command = input(">> Enter plugin $ ")

                if(user_command == "q" or user_command == "exit" or user_command == "quit"):
                    print("Goodbye...")
                    exit()
                elif(user_command == "help"):
                    help()
                    continue
                elif(user_command == "cp" or user_command == "cprofile"):
                    if(version != "3"):
                        profile_name = input(">>> New profile # ")
                        print("INFO:    profile changed to "+profile_name)
                    else:
                        print("INFO: Command not available in volatility 3.")
                    continue
                elif(user_command == "shell"):
                    while(True):
                        try:
                            shellcmd = input(">>> Shell command % ")
                            if(shellcmd == "q" or shellcmd == "quit" or shellcmd == "exit"):
                                break
                            else:
                                os.system(shellcmd)
                                continue
                        except KeyboardInterrupt:
                            print("User Interupted...")
                            continue
                    continue
                elif(user_command == "" or user_command == " "):
                    print("You must specify something to do (try -h)")
                    continue
                else:
                    if(version == "3"):
                        if(os.system(volatility+" -f "+imageName+" "+user_command) != 0):
                            pass
                        continue
                    else:
                        if(os.system(volatility+" -f " +imageName+" --profile=" +profile_name+" "+user_command) != 0):
                            pass
                        continue
        except KeyboardInterrupt:
            print("KeyboardInterrupt: To exit type q, exit or quit")
            continue
