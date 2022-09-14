def save_thumbnail(event):
    import os
    import shutil
    from glob import glob

    from util.button.path import product_path as pp
    from view.gui import save_folder_name, save_state

    product_path = str(pp())

    if product_path == "None":
        print(product_path)
        # wx.MessageDialog(None, "경로를 설정해 주세요", "에러", wx.OK | wx.ICON_ERROR, pos=(200, 200)).ShowModal()
        return

    # image_path = glob(
    #     os.path.join(
    #         product_path,
    #         "*%s*" % "촬영",
    #     )
    # )[0]

    image_path = product_path

    temp = "\\".join(product_path.split("\\")[:-1])
    save_path = os.path.join(temp, "web", "product", save_folder_name.get())
    # print(product_path)
    # print(image_path)
    # print(save_path)
    if not os.path.isdir(save_path):
        os.makedirs(save_path)

    file_list = glob(os.path.join(image_path, "*/*_1.jpg"))
    for i in file_list:
        shutil.copy(i, save_path + "\\" + i.split("\\")[-1])

    save_state.configure(text="사진 복사 상태 : " + str(len(file_list)) + "개 이미지 복사완료")
