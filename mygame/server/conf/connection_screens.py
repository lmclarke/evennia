# -*- coding: utf-8 -*-
"""
Connection screen

Texts in this module will be shown to the user at login-time.

Evennia will look at global string variables (variables defined
at the "outermost" scope of this module and use it as the
connection screen. If there are more than one, Evennia will
randomize which one it displays.

The commands available to the user when the connection screen is shown
are defined in commands.default_cmdsets. UnloggedinCmdSet and the
screen is read and displayed by the unlogged-in "look" command.

"""

from django.conf import settings
from evennia import utils

CONNECTION_SCREEN = """
|W            .        +          .      .          .
|W     .            |Y_|W        .                    .
|y  ,              |Y/;-._,-.____        ,-----.__
|y (( |W       .    |Y(_:#::_.:::. `-._   /:, /-._, `._,
|y  `|W                 \   _| |Y"=:_::.`.);  \ __/ /|W
|W                      ,    `./ |Y \:. `.   )==-'  |W.
|W    .|Y      ., ,-=-.  |W,\, |x+#|W./`   |Y\:.  / /          |W .
|W.|Y           \/:/`-'|W , ,\ '` ` `   |Y): , /    
|W       . |Y   /:|W+- - + +- : :- + + -|Y:'  /            .
|W  .      |Y,=':  \|W    ` `/` ' , , ,|Y:' `'--".--"---._/`7|W
|W   `.   |Y(    \: \,-._|W` ` + '\, |Y,"   _,--._,---":.__/|W
|Y              \:  `  X` |W_| _,\|Y/'   .-'|W
|W.               |Y":._:`\____  /:'  /|W      .           .
|Y                    \::.  :\/:'  /|W              +
|G          =================================|W
            _,,   , _,,  , ___,___, ,_   _, 
           /_,\  / /_,|\ |' | ' |   | \,/_, 
          '\_  \/`'\_ |'\|  |  _||_,_||_/'\_  
             ` '     `'  `  ' '   '       `
|G          =================================|W
|Y                   .  |::.     ,`|W                  .
|Y     .                |::.    | |W
|Y                      |::.\  \ `.|W
|Y                      |::::\    | |W
|w              O      |Y |:::/( )  |                 |G (|co|W
|G               )  |Y___/#\::`/ (O "==._____|W  |c O|G, (|WO|G  /` |W
 Connect to an existing account:|C connect username password|W
 Create an account: |Ccreate username password|W
 Enter |Chelp|n for more info. |Clook|n will re-show this screen.

 Welcome to |w{}|n, version |w{}|n.
""" \
    .format(settings.SERVERNAME, utils.get_evennia_version())
