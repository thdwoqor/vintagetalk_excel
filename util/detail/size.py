from pywinauto.application import Application


def size(title: str, class_name: str):
    try:
        app = Application(backend="win32").connect(title_re=title, class_name=class_name)
        dlg_spec = app.window(title=title, found_index=0)
        size_x = dlg_spec.rectangle().right - dlg_spec.rectangle().left
        size_y = dlg_spec.rectangle().bottom - dlg_spec.rectangle().top
    except Exception as e1:
        return False
    return size_x, size_y, dlg_spec.rectangle().top, dlg_spec.rectangle().left
