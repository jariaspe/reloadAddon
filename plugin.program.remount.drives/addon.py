import xbmcaddon
import xbmcgui
import os


addon 		= xbmcaddon.Addon()

dialogTitle = addon.getLocalizedString(32000)
dialogText = addon.getLocalizedString(32001)
okText = addon.getLocalizedString(32002)

dialog = xbmcgui.Dialog()

class Remount():
	def lauch(self):
		os.system("mount -o loop /dev/sda /media/DiscoRasp/")
		dialog.ok(dialogTitle, okText)


remount = Remount()


if dialog.yesno(dialogTitle, dialogText):
	remount.lauch()

del dialog
del remount