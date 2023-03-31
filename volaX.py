#! /usr/bin/python3

####################################################################################################################
# PLEASE NOTE: THIS IS NOT A NEW IMPLEMENTATION OF VOLATILITY. IT SIMPLY USES THE VERSION OF VOLATILITY            #
# (specifically volatility 2). This simple program aims to simply ease the use of volatility.                      #
# It saves the imageName of the image all you have to do is focus on other commands to accomplish your task.       #
# To change imageName use cp or cimageName, a prompt will follow for you to enter another imageName.               #
####################################################################################################################

####################################################################################################################
# WRITTEN BY: SAMOH MOHAMMED. TWITTER @ghostshado3. GITHUB @samohtechs, Website: https://samohtechs.tk             #
# you can clone or fork this work here www.twitter.com/samohtechs/volaX                                            #
####################################################################################################################

import subprocess as sub
import shlex

def help():
	print("Welcome To Volatility!")
	print("USAGE:")
	print("help           this help")
	print("--help 		  volatility help menu")
	print("cp, cprofile   change profile name (when profile has already been selected)")
	print("q, exit, quit  exit program and return to shell")
	print("shell          to enter shell commands mode")
	print("")

def volatility(volatility, version="2", path=None):
    while(True):
        ## Read image or Image Name...
        imageName = input(">> Enter name of image: ")
        try:
            if(imageName == "q" or imageName == "exit" or imageName == "quit"):
                print("Goodbye...")
                break
            elif(imageName == "help"):
                help()
                continue
            elif(imageName == "cp" or imageName == "cprofile"):
                print("INFO: Cannot change profile. No profile has been used yet.")
                continue
            elif(imageName == "" or imageName == " "):
                print("ALERT: File name not supplied...")
                continue
            else:
                # Check volatility version
                if(version == "2"):
                    profile_name = input(">> Enter profile name (leave blank to run imageinfo): ")

                    if(profile_name == "" or profile_name == " "):
                        try:
                            # Execute the commands using subprocess
                            if(sub.run([volatility, "-f", imageName, "imageinfo"], shell=False)):
                                pass
                            # Allow user to provide profile name here
                            profile_name = input("\n>> Enter profile name to use: ")
                        except sub.CalledProcessError as e:
                            print("ERROR: Command execution error")
                    else:
                        pass
                    break
                elif(version == "3"):
                    profile_name = "P:None"
                    break
                else:
                    break
        except FileNotFoundError:
            print("ERROR: File Not Found...")
            continue
        except KeyboardInterrupt:
            print("KeyboardInterrupt: To exit type q, exit or quit")
        except sub.CalledProcessError as e:
            print("ERROR: command execution error: ", e)
            continue
        except:
            print("Unexpected error occoured")

    while(True):
        try:
            if(profile_name == "" or profile_name == " "):
                print("ALERT: Please provide a profile name...")
                profile_name = input("\n>> Enter profile name to use: ")
                continue
            else:
                if(path == None):
                    print("")
                else:
                    print("\n(PATH: "+volatility+")")

                if(version == "3"):
                    print("(volatility -f "+imageName+")")
                else:
                    print("(volatility -f "+imageName+" --profile="+profile_name+")")

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
                        if(profile_name == "" or profile_name == " "):
                            print("Profile cannot be empty")
                            continue
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
                                try:
                                    sanitized_cmd = sub.list2cmdline(shlex.split(shellcmd))
                                    sub.run(sanitized_cmd, shell=True)
                                    continue
                                except sub.CalledProcessError as e:
                                    print("ERROR: command execution error. " + e)
                                except:
                                    print("Error: Unexpected error occured.")
                        except KeyboardInterrupt:
                            print("User Interupted...")
                            continue
                    continue
                elif(user_command == "" or user_command == " "):
                    print("You must specify something to do (try -h)")
                    continue
                else:
                    try:
                        if(version == "3"):
                            sub.run([volatility, "-f", imageName, user_command], shell=False)
                            continue
                        else:
                            if(sub.run([volatility, "-f", imageName, "--profile=" + profile_name, user_command], shell=False)):
                                pass
                            continue
                    except sub.CalledProcessError as e:
                        print("ERROR: command execution error. " + e)
                    except:
                        print("Error: Unexpected error occured.")
        except KeyboardInterrupt:
            print("KeyboardInterrupt: To exit type q, exit or quit")
            continue
