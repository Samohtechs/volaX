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
    # WRITTEN BY: SAMOH MOHAMMED. TWITTER @_cyb3rwolf. GITHUB @samohtechs.                                     #
    # LINKEDIN: https://www.linkedin.com/in/samoh-mohammed/ PORTFOLIO: https://samohtechs.com                  #
    # you can clone or fork this work here www.github.com/samohtechs/volaX                                     #
    ############################################################################################################
    
   # __REQUIREMENTS__
  > - python 3.x <br>
  > - volatility (version 2 or 3) <br>
  > - volatility must be accessible globally as 'volatility' for volatility 2 and 'volatility3' for volatility 3 or you can add your own path in 
      the file __volpath.py__ as required.
  
  # __USAGE:__
  > - __help__           _this help_ <br>
  > - __--help__           _volatility help menu_ <br>
  > - __cp, cprofile__   _change profile name (when profile has already been selected)_ <br>
  > - __q, exit, quit__  _exit program_ <br>
  > - __shell__          _to enter shell commands mode_ <br>
  
  ## Running the script:
  Run __python3 vola.py__ <br>
  or <br>
  __./vola__ (this is a bash script that runs python3 vola.py. Make sure to run chmod +x ./vola to give executable permission.). Then, <br>
  
  __You will have to select one option from five options given that are__ <br>
  > 1 - To specify your own path and version (be keen with version as it will result to unexpected behaviour when used with wrong volatility) <br>
  > 2 - Volatility 2 <br>
  > 3 - Volatility 3 <br>
  > 4 - To use your own path and version that you have set in the specific variables found in the __volpath.py__ file. So next time you want to use that           simply select 4. <br>
  > 0 - to exit <br>
  
  ## FOR USE WITH VOLATILITY 2:
  After running the script and selecting option 1 (or 3, or 4 and specify your path and version as 2), you will then be asked to enter the image name/ full path <br>
  
    >> Enter name of image: /path/to/image
  then
  
    >> Enter profile name (leave blank to run imageinfo):
  
  Pressing enter (if no profile specified), it will run _imageinfo_ and bring you to the next prompt to allow you to enter the profile name which you can find in the _"Suggested Profile(s)"_
  
    >> Enter profile name to use: Win7SP1x64
  
  Now from there another prompt will be given where you only have to enter specific plugins to use with the profile. Above the prompt will be the full path to your image and the profile
  
    (volatility -f /path/to/memoryimage --profile=Win7SP1x64)
    >> Enter plugin $ pstree

  ### To change the profile.
  just enter cp or cprofile like, __>> Enter plugin $ cp__ or __>> Enter plugin $ cprofile__. a prompt to allow you to enter new profile will follow
  
    >>> New Profile % newProfile
  
  Now you new profile will be reflected.
  
  ### To execute Shell/Terminal commands
  Enter shell in the prompt _>> Enter plugin $ shell_
  
    >>> Shell command % ifconfig
  
  enter __exit__ to go back to previous prompt.
  
  And that is All!
  
  ## FOR USE WITH VOLATILITY 3:
  Everything is just the same as in volatility 2 with small difference when you first run the script <br>
  
  > 1. Select option 2 to use volatility 3 (or 3, or 4 and specify your path and version as 2), you will then be asked to enter the image name/ full path <br>
  
    >> Enter name of image: /path/to/image
  
  Pressing enter will bring you to the prompt where you can continue providing other plugins for use.
  
    (volatility -f /path/to/memoryimage)
    >> Enter plugin $ pstree
  
  And that is All!
  
  HOPE THIS SIMPLE TOOL MAKES YOUR WORK A LITTLE LESS TIRESOME 😊
