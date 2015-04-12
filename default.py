import xbmc,xbmcaddon,xbmcgui,os,sys
from elementtree.SimpleXMLWriter import XMLWriter

settings = xbmcaddon.Addon( id = 'script.service.usbspindown' )
userdata = xbmc.translatePath('special://userdata/keymaps')

#interval in minutes
interval=5
#disck to check
disk="sda"

def getstate(name):
    for r in open("/proc/diskstats"):
        if r[2]==name:
           return r



addon=xbmcaddon.Addon()
addonname=addon.getAddonInfo('name')

p=addon.getAddonInfo('path')
os.chdir(p)
os.system("chmod a+x sdparm")


state=getstate(disk)

while (not xbmc.abortRequested):
    xbmc.sleep(interval*60000)
    #xbmcgui.Dialog().ok(addonname,"ciao","mondo",p)
    newstate=getstate(disk)
    if state==newstate:
        os.system("LD_LIBRARY_PATH=. ./sdparm -f -C stop /dev/%s"%disk)
