import xbmcaddon
import xbmcgui

addon 		= xbmcaddon.Addon()
addonname 	= addon.getAddonInfo('name')

class Remount(xbmc):
	def lauch(self):
		print "init launch"
		xbmcgui.Dialog().ok("Works", "Ok clicked")

print "after Remount definition"
remount = Remount()
print "after remount object instantation"
dialog = xbmcgui.Dialog()
print "after dialog instantation"

if dialog.yesno("addonname", "Remount drives"):
	print "if yesno clicked"
	remount.lauch()

del dialog
del remount