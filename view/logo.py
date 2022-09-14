def logo():
    import io
    import urllib.request
    from tkinter import Label

    from PIL import Image, ImageTk

    from view.gui import root

    try:
        url = "https://vintagetalk.co.kr/_/header/images/logo_vintagefarm.png"

        def ImgFromUrl(url):
            global image
            with urllib.request.urlopen(url) as connection:
                raw_data = connection.read()
            im = Image.open(io.BytesIO(raw_data))
            image = ImageTk.PhotoImage(im)
            return image

        logo = Label(root, image=ImgFromUrl(url))
        logo.pack(pady=20)
    except:
        root.geometry("250x800")
