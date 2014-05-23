import wx

class MainFrame(wx.Frame):    

    def __init__ (self):
        wx.Frame.__init__(self, parent=None)
        panel= wx.Panel(parent=self)
        box = wx.BoxSizer(wx.HORIZONTAL)
        panel.SetSizer(box)

        button1 = wx.Button(parent=panel, label="Button1")
        button2 = wx.Button(parent=panel, label="Button2")
        box.Add(button1, proportion=1)
        box.Add(button2, proportion=3)

        self.Show(True)

        check = wx.CheckBox(parent=panel, label="checkBox")
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox, check)
        box.Add(check, proportion=10)

    def on_checkbox(self, evt):
        print "Ausgabe"

app=wx.PySimpleApp()
frame = MainFrame()
app.MainLoop()
