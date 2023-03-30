    ***   *** ******** ****         ****            ****   ****
    ***   *** ******** ****      ***    ***          **** ****
    ***   *** ***  *** ****      ***    ***           ******
    ***   *** ***  *** ****      **********           ******
    ***   *** ***  *** ****      **********         **** ****
     *** ***  ******** ********* ***    ***        ****   ****
      ****    ******** ********* ***    ***       ****     **** v1.0
      
    Memory Forensics made Easy!""")

    ############################################################################################################
    # PLEASE NOTE: THIS IS NOT A NEW IMPLEMENTATION OF VOLATILITY. IT SIMPLY USES THE VERSION OF VOLATILITY    #
    # (specifically volatility 2). This simple program aims to simply ease the use of volatility.              #
    # It saves the profile of the image all you have to do is focus on other commands to accomplish your task. #
    # To change profile use cp or cprofile, a prompt will follow for you to enter another profile.             #
    ############################################################################################################

    ############################################################################################################
    # WRITTEN BY: SAMOH MOHAMMED. TWITTER @ghostshado3. GITHUB @samohtechs. Website: https://samohtechs.tk     #
    # you can clone or fork this work here www.github.com/samohtechs/volaX                                     #
    ############################################################################################################

  # __USAGE:__
  __help__           _this help_ <br>
  __help__           _volatility help menu_ <br>
  __cp, cprofile__   _change profile name (when profile has already been selected)_ <br>
  __q, exit, quit__  _exit program_ <br>
  __shell__          _to enter shell commands mode_ <br>
  
  ### When Running the script
  __You will have to select one option from five options given that are__ <br>
  1 - Volatility 2 <br>
  2 - Volatility 3 <br>
  3 - To specify your own path and version (be keen with version as it will result to unexpected behaviour when used with wrong volatility) <br>
  4 - To specify your own path and version but this time in the specific variables found the the __volpath.py__ file. <br>
  So next time you want to use that simply select 4
  0 - to exit <br>
  
  ## FOR USE WITH VOLATILITY 2:
  After running the script and selecting option 1 (or 3, or 4 and specify your path and version as 2), you will then be asked to enter the image name/ full path <br>
  
    >> Enter name of image: /path/to/image
  
  Pressing enter, it will run imageinfo and bring you to the next prompt to allow you to enter the profile name which you can find in the "Suggested Profile(s)"
  
    >> Enter profile name to use: Win7SP1x64
  
  Now from there another prompt will be given where you only have to enter specific plugins to use with the profile. Above the prompt will be she full path to your image and the profile
  
    (volatility -f /path/to/memoryimage --profile=Win7SP1x64)
    >> Enter plugin $ pstree

  ### To change the profile.
  just enter cp or cprofile like, __>> Enter plugin $ cp__ or __>> Enter plugin $ cprofile__. a prompt to allow you to enter new profile will follow
  
    >>> New Profile % newProfile
  
  Now you new profile will be reflected.
  
  ### To execute Shell/Terminal commands
  Enter shell in the prompt >> Enter plugin $ shell
  
    >>> Shell command % ifconfig <br>
  
  enter __exit__ to go back to previous prompt.
  
  And that is All!
  
  # FOR USE WITH VOLATILITY 3
  Everything is just the same as in volatility 2 with small difference when you first run the script <br>
  
  1. Select option 2 to use volatility 3 (or 3, or 4 and specify your path and version as 2), you will then be asked to enter the image name/ full path <br>
  
  __>> Enter name of image: /path/to/image__
  
  Pressing enter, it will run windows.info and bring you to the prompt where you can continue providing other plugins for use.
  
    (volatility -f /path/to/memoryimage)
    >> Enter plugin $ pstree
  
  And that is All!
  
  HOPE THIS SIMPLE TOOL MAKES YOUR WORK A LITTLE TIRESOME 😊
