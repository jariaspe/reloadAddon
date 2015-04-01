import xbmcaddon
import xbmcgui
import xbmc
import os


addon 		= xbmcaddon.Addon()
addonname 	= addon.getAddonInfo('name')

class Remount():
	def lauch(self):
		xbmc.log("init launch")
		os.system("mount -o loop /dev/sda /media/DiscoRasp/")

xbmc.log("after Remount definition")
remount = Remount()
xbmc.log("after remount object instantation")
dialog = xbmcgui.Dialog()
xbmc.log("after dialog instantation")

if dialog.yesno("addonname", "Remount drives"):
	xbmc.log("if yesno clicked")
	remount.lauch()

del dialog
del remount
xbmc.log("end of file")
