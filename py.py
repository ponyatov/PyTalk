import os,sys,wx

app = wx.App()

frmMain = wx.Frame(None,-1,os.getcwd())
frmMain.SetIcon(wx.Icon('logo64x64.ico'))



frmMain.Show()

app.MainLoop()

