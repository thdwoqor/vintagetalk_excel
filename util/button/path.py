import wx

if "app" not in locals():
    app = wx.App(None)


def DirDialog(DefaultDir="", Title="Select Directory:"):
    dlg = wx.DirDialog(None, Title, DefaultDir, wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
    if dlg.ShowModal() == wx.ID_OK:
        DirName = dlg.GetPath()
    else:
        DirName = None
    dlg.Destroy()

    return DirName


def product_path():
    # dialog = wx.DirDialog(None, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    dialog = wx.DirDialog(None, "폴더 선택", "", wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
    if dialog.ShowModal() == wx.ID_OK:
        image_path = dialog.GetPath()
        print(image_path)
    else:
        image_path = None
    dialog.Destroy()
    return image_path
