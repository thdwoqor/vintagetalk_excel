def save(event):
    import configparser
    from tkinter import messagebox

    from view.gui import (
        blank_size,
        f9_image_state,
        f9_state,
        line_color,
        merge_folder_name,
        save_folder_name,
        var,
        width_size,
    )

    widgets = [
        (f9_state, "f9_state"),
        (f9_image_state, "f9_image_state"),
        (save_folder_name, "folder_name"),
        (merge_folder_name, "merge_folder_name"),
        (blank_size, "blank_size"),
        (width_size, "width_size"),
    ]

    with open("conf.ini", "w") as configfile:
        config = configparser.ConfigParser()
        for widget, name in widgets:
            config["DEFAULT"][name] = str(widget.get())
        config["DEFAULT"]["var"] = str(var.get())
        config["DEFAULT"]["line_color"] = str(line_color.cget("bg"))

        config.write(configfile)
    messagebox.showinfo("Save", "Save Complete!")
