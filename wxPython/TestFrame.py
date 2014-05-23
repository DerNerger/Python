import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="halloworld", size=(1200,800), pos=(20,20))

        panel = wx.Panel(parent=self)
        
  
        button = wx.Button(parent=panel, label="close", pos=(400,10))
        self.Bind(wx.EVT_BUTTON, self.on_button1, button)
        
        button2 = wx.Button(parent=panel, label="Button2")
        button2.SetSize((300,300)) 
        self.Bind(wx.EVT_BUTTON, self.on_button2, button2)

        wx.StaticText(parent=panel, label="this is text", style=wx.ALIGN_RIGHT, pos=(300,300))
 
        self.Show(True)
        
    def on_button1(self, evt):
        self.Close(True)

    def on_button2(selv, evt):
        print "btn 2 wurde gedrueckt"

app = wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
