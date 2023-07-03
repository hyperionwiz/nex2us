import os, xbmcaddon
#########################################################
### User Edit Variables #################################
#########################################################
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[COLOR mediumslateblue]-[B]Nex2us Wizard[/B]-[/COLOR]'
BUILDERNAME    = 'The Hood'
#########################Make sure to change the repo to yours!!!!
EXCLUDES       = [ADDON_ID, 'roms', 'My_Builds', 'backupdir', 'script.module.kodi-six', 'script.module.six']
BUILDFILE      = 'https://filedn.com/l0jm1ttNAy54e9NylPPsPVk/Nexus/texts/builds.txt'
UPDATECHECK    = 0
APKFILE        = 'https://filedn.com/l0jm1ttNAy54e9NylPPsPVk/Nexus/texts/apk_file.xml'
YOUTUBETITLE   = 'FTG Help Videos' 
YOUTUBEFILE    = 'http://'
ADDONFILE      = 'http://'
ADVANCEDFILE   = 'http://'
ROMPACK        = 'http://'
EMUAPKS        = 'http://'
ADDONPACK      = 'http://'
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################

##Alway test to see the color combo!!

#### NEW GUI THEME ###################################
# Choose from the following 
# Only these colors avalable
# white , blue , orange , yellow , red , purple , pink , lime , cyan, green
#Button focus color
FOCUS_BUTTON_COLOR = 'blue'
EXIT_BUTTON_COLOR = 'red'
#Highlight outline for lists
HIGHLIGHT_LIST = 'button_focus'
HIGHLIGHT_LIST2 = 'MenuItemFO'
##No TXT file Banner
NO_TXT_FILE = 'pink'

############################################
############################################
### The full list of colors for below can found @ https://forum.kodi.tv/showthread.php?tid=210837

#Top Main buttons
MAIN_BUTTONS_TEXT = 'white'
#All other buttons
OTHER_BUTTONS_TEXT = 'white'
#all list text color
##FYI any color placed in the txt file will overide this
LIST_TEXT = 'white'


#Description text title color
DES_T_COLOR = 'white'
#Description color
DESCOLOR = 'aliceblue'

#Wizard title name and verion color
WIZTITLE = 'Nex2us Wizard'
WIZTITLE_COLOR = 'white'
VERTITLE_COLOR = 'white'
VER_NUMBER_COLOR = 'snow'
############################################################

## The colors and theme below is still used for the pop up dialogs
##Alway test to see the color combo
# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'white'
COLOR2         = 'cyan'
COLOR3         = 'red'
COLOR4         = 'snow'
COLOR5         = 'cyan'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR2+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR2+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
THEME6         = '[COLOR '+COLOR3+'][B]%s[/B][/COLOR]'



#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://filedn.com/l0jm1ttNAy54e9NylPPsPVk/Docs/Pics/icon.png'
ICONMAINT      = 'https://filedn.com/l0jm1ttNAy54e9NylPPsPVk/Docs/Pics/icon.png'
ICONAPK        = 'https://filedn.com/l0jm1ttNAy54e9NylPPsPVk/Docs/Pics/icon.png'
ICONADDONS     = 'https://filedn.com/l0jm1ttNAy54e9NylPPsPVk/Docs/Pics/icon.png'
ICONYOUTUBE    = 'https://filedn.com/l0jm1ttNAy54e9NylPPsPVk/Docs/Pics/icon.png'
ICONSAVE       = 'https://filedn.com/l0jm1ttNAy54e9NylPPsPVk/Docs/Pics/icon.png'
ICONTRAKT      = 'https://filedn.com/l0jm1ttNAy54e9NylPPsPVk/Docs/Pics/icon.png'
ICONREAL       = 'https://filedn.com/l0jm1ttNAy54e9NylPPsPVk/Docs/Pics/icon.png'
ICONLOGIN      = 'https://filedn.com/l0jm1ttNAy54e9NylPPsPVk/Docs/Pics/icon.png'
ICONCONTACT    = 'https://filedn.com/l0jm1ttNAy54e9NylPPsPVk/Docs/Pics/icon.png'
ICONSETTINGS   = 'https://filedn.com/l0jm1ttNAy54e9NylPPsPVk/Docs/Pics/icon.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '~'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = ''
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = os.path.join(ART, 'icon.png')
CONTACTFANART  = 'http://'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = 'http://'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'http://'
# Url to folder zip is located in
REPOZIPURL     =  'http://'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'https://filedn.com/l0jm1ttNAy54e9NylPPsPVk/Nexus/texts/notify1.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font16'
HEADERMESSAGE  = 'Nex2us Wizard'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Font for Notification Window
FONTSETTINGS   = 'Font14'
# Background for Notification Window
BACKGROUND     = os.path.join(ART, 'ContentPanel.png')
BACKGROUND2     = os.path.join(ART, 'ContentPanel.png')
BACKGROUND3     = os.path.join(ART, 'ContentPanel.png')
############################    #############################