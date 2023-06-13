from tkinter import Tk, Label, Button, filedialog
from PIL import ImageTk, Image
import subprocess

def open_python_file():
    file_path = "D:/Project/Python/YoloV5/Final_Project.py"
    subprocess.Popen(["python", file_path])
    root.destroy()

def import_image():
    global file_path
    logo_path = 'D:/Project/Python/YoloV5/Image_final_project/Khoa_CKM.png'
    logo = Image.open(logo_path)
    
    hieu_path = 'D:/Project/Python/YoloV5/Image_final_project/Hieu.png'
    hieu = Image.open(hieu_path)
    
    thach_path = 'D:/Project/Python/YoloV5/Image_final_project/Thach.png'
    thach = Image.open(thach_path)
    
    loc_path = 'D:/Project/Python/YoloV5/Image_final_project/Loc.png'
    loc = Image.open(loc_path)

    ThayThai_path = 'D:/Project/Python/YoloV5/Image_final_project/Thay_Thai.png'
    ThayThai = Image.open(ThayThai_path)
    
    # Resize the image if needed
    logo = logo.resize((600, 100), Image.ANTIALIAS)
    hieu = hieu.resize((150, 150), Image.ANTIALIAS)
    thach = thach.resize((100, 170), Image.ANTIALIAS)
    loc = loc.resize((100, 190), Image.ANTIALIAS)
    ThayThai = ThayThai.resize((100, 150), Image.ANTIALIAS)

    # Convert the image to Tkinter-compatible format
    logo_photo = ImageTk.PhotoImage(logo)
    hieu_photo = ImageTk.PhotoImage(hieu)
    thach_photo = ImageTk.PhotoImage(thach)
    loc_photo = ImageTk.PhotoImage(loc)
    ThayThai_photo = ImageTk.PhotoImage(ThayThai)

    # Create a label to display the image
    logo_label = Label(root, image=logo_photo)
    logo_label.image = logo_photo  # type: ignore # Keep a reference to prevent garbage collection
    logo_label.place(x=60, y=2)
    
    hieu_label = Label(root, image=hieu_photo)
    hieu_label.image = hieu_photo  # type: ignore # Keep a reference to prevent garbage collection
    hieu_label.place(x=-10, y=300)
    
    thach_label = Label(root, image=thach_photo)
    thach_label.image = thach_photo  # type: ignore # Keep a reference to prevent garbage collection
    thach_label.place(x=150, y=280)
    
    loc_label = Label(root, image=loc_photo)
    loc_label.image = loc_photo  # type: ignore # Keep a reference to prevent garbage collection
    loc_label.place(x=300, y=270)
    
    ThayThai_label = Label(root, image=ThayThai_photo)
    ThayThai_label.image = ThayThai_photo  # type: ignore # Keep a reference to prevent garbage collection
    ThayThai_label.place(x=460, y=302)
    


root = Tk()
root.title("Main Window")
root.geometry("600x600")


# Create a label for the tittle
tittle_label = Label(root, text="CÔNG NGHỆ KỸ THUẬT CƠ ĐIỆN TỬ",
                      font = ("Times New Roman", 16,"bold"), fg = "black")
tittle_label.place(x = 120, y = 120)

# Create a label for the Hieu
tittle_label = Label(root, text="Trần Ngọc Hiểu\nMSSV: 20146127",
                      font = ("Times New Roman", 9,"bold"), fg = "black")
tittle_label.place(x = 10, y = 460)

# Create a label for the Thach
tittle_label = Label(root, text="Nguyễn Bá Vũ Thạch\nMSSV: 20146530",
                      font = ("Times New Roman", 9,"bold"), fg = "black")
tittle_label.place(x = 150, y = 460)

# Create a label for the Loc
tittle_label = Label(root, text="Lê Tấn Lộc\nMSSV: 20146121",
                      font = ("Times New Roman", 9,"bold"), fg = "black")
tittle_label.place(x = 310, y = 460)

# Create a label for Thay Thai
tittle_label = Label(root, text="GVHD\nTS.Nguyễn Văn Thái",
                      font = ("Times New Roman", 9,"bold"), fg = "black")
tittle_label.place(x = 450, y = 460)

# Create a label for the the major
tittle_label = Label(root, text="Hệ thống hỗ trợ nhận dạng và kiểm đếm số lượng \nlinh kiện điện tử trên bo mạch",
                      font = ("Times New Roman", 18, "bold", "italic"), fg = "red")
tittle_label.place(x = 60, y = 180)
# Call the import_image function to display the image automatically
import_image()

#Create a button to go to the program
open_button = Button(root, text="Open", font = ("Arial", 11, "bold"), command=open_python_file, bg="blue", fg="white", width= 15, height=2)
open_button.place(x = 230, y = 520)

root.mainloop()
