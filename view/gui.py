import tkinter.font as font
from tkinter import (
    BooleanVar,
    Checkbutton,
    DoubleVar,
    Entry,
    IntVar,
    Label,
    Scale,
    Tk,
    ttk,
)

from util.button.color import choice_color
from util.button.merge import merge_all
from util.button.save import save
from util.button.thumbnail import save_thumbnail


root = Tk()
root.title("")
root.geometry("330x400")
f = font.Font(size=10)

# f9_state
f9_state = BooleanVar()
f9_btn = Checkbutton(root, text="Enter F9 활성화", variable=f9_state, font=f)
f9_btn.pack()

f9_image_state = BooleanVar()
image_btn = Checkbutton(root, text="등록 이미지 F9 활성화", variable=f9_image_state, font=f)
image_btn.pack()

var = IntVar()
scale = Scale(root, variable=var, orient="horizontal", from_=1, to=5).pack()

Label(root, text="스크롤 속도 조절", font=f).pack()

save_btn = Label(root, text="Save", bg="grey19", fg="snow", width=20, height=2, font=f)
save_btn.bind("<Button-1>", save)
save_btn.pack(pady=10)

# logo()

# horizontal line
line = ttk.Separator(root, orient="horizontal")  # or vertical
line.pack(fill="both")

# save folder name
save_folder_label = Label(root, width=50, height=7, font=f)
save_folder_label.pack(pady=7)
Label(save_folder_label, text="저장할 폴더명 : ", font=f).pack(side="left")
save_folder_name = Entry(save_folder_label, width=10, font=f)
save_folder_name.pack(side="left")

# save thumbnail
save_state = Label(root, text="사진 복사 상태 : 대기중", font=f)

save_thumbnail_btn = Label(root, text="사진 복사", bg="grey19", fg="snow", width=20, height=2, font=f)
save_thumbnail_btn.bind("<Button-1>", save_thumbnail)
save_thumbnail_btn.pack(pady=5)

save_state.pack(pady=5)

# horizontal line
line = ttk.Separator(root, orient="horizontal")  # or vertical
line.pack(fill="both", pady=5)

# merge folder name
blank_label = Label(root, width=300, height=7, font=f)
blank_label.pack(anchor="nw")
Label(blank_label, text="공백 : ", font=f).pack(side="left")
blank_size = Entry(blank_label, width=7, font=f)
blank_size.pack(side="left")
Label(blank_label, text="px", font=f).pack(side="left", padx=5)

save_merge_btn = Label(blank_label, text="변환", bg="grey19", fg="snow", width=10, height=2, font=f)
save_merge_btn.bind("<Button-1>", merge_all)
save_merge_btn.pack(side="left", padx=10)

Label(blank_label, text="저장할 폴더명", font=f).pack(side="left")

# width
width_label = Label(root, width=300, height=7, font=f)
width_label.pack(pady=5, anchor="nw")
Label(width_label, text="너비 : ", font=f).pack(side="left")
width_size = Entry(width_label, width=7, font=f)
width_size.pack(side="left")
Label(width_label, text="px", font=f).pack(side="left", padx=5)

line_color = Label(width_label, text="", bg="grey19", fg="snow", width=10, height=2, relief="ridge", font=f)
line_color.bind("<Button-1>", choice_color)
line_color.pack(side="left", padx=10)

merge_folder_name = Entry(width_label, width=10, font=f)
merge_folder_name.pack(side="left")

# horizontal line
line = ttk.Separator(root, orient="horizontal")  # or vertical
line.pack(fill="both")

merge_s = Label(root, width=200, height=7, font=f)
merge_s.pack(pady=5)
merge_state = DoubleVar()
merge_progressbar = ttk.Progressbar(merge_s, maximum=100, length=100, variable=merge_state)
merge_progressbar.pack(side="left", padx=5)
merge_progress = Label(merge_s, text="대기중", font=f)
merge_progress.pack(side="left")
