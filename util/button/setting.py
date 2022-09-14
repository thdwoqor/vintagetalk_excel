def setting():
    import configparser

    from view.gui import (
        blank_size,
        f9_btn,
        image_btn,
        line_color,
        merge_folder_name,
        save_folder_name,
        var,
        width_size,
    )

    config = configparser.ConfigParser()
    config.read("conf.ini")

    widgets_check = [(f9_btn, "f9_state"), (image_btn, "f9_image_state")]
    widgets_textbox = [
        (save_folder_name, "folder_name"),
        (merge_folder_name, "merge_folder_name"),
        (blank_size, "blank_size"),
        (width_size, "width_size"),
    ]
    try:
        for widget, name in widgets_textbox:
            widget.insert(0, config["DEFAULT"][name])
        for widget, name in widgets_check:
            if config["DEFAULT"][name] == "True":
                widget.toggle()
        var.set(int(config["DEFAULT"]["var"]))
        line_color.config(bg=config["DEFAULT"]["line_color"])
    except Exception as e1:
        print(e1)
