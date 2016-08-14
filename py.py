import os,sys,wx
import meta

app = wx.App()

frmMain = wx.Frame(parent=None,id=-1,title=os.getcwd())
frmMain.SetIcon(wx.Icon('logo64x64.ico'))
frmMain.Maximize()
frmMain.Show()

menu = wx.MenuBar()
frmMain.SetMenuBar(menu)

menuFile = wx.Menu()
menu.Append(menuFile,'&File')

def OnQuit(e):
	frmMain.Close()
menuQuit = menuFile.Append(wx.ID_EXIT,'&Quit')
frmMain.Bind(wx.EVT_MENU,OnQuit,menuQuit)

menuHelp = wx.Menu()
menu.Append(menuHelp,'&Help')
menuAbout = menuHelp.Append(wx.ID_ABOUT,'&About\tF1')
def OnAbout(e):
	info = wx.AboutDialogInfo()
	info.Name = meta.Title
	info.Version = meta.Version
	info.Copyright = meta.Copyright
	info.Description = meta.About
	info.WebSite = meta.GitHub
#	info.License  = meta.License
#	info.Developers = meta.Author
	wx.AboutBox(info)
frmMain.Bind(wx.EVT_MENU,OnAbout,menuAbout)

app.MainLoop()

