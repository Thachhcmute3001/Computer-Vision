from tkinter import Tk, Label, Button, filedialog, Checkbutton, IntVar, Toplevel
from PIL import ImageTk, Image, ImageDraw
import torch
import numpy as np
import cv2
import subprocess

# List of component labels
component_labels = ["Transistor SMD", "Cap SMD", "Res SMD", "IC", "Cap Throughhole", "Crystal", "Diode", "Res Throughhole"]

# Create a list to store the selected components
selected_components = []

def load_model():
    global model
    path = filedialog.askopenfilename()
    model = torch.hub.load('ultralytics/yolov5', 'custom', path)  # custom trained model
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device).eval()

# Function to handle checkbox selection
def checkbox_changed(component_index, var):
    if var.get() == 1:
        selected_components.append(component_labels[component_index])
    elif component_labels[component_index] in selected_components:
        selected_components.remove(component_labels[component_index])

def start_detection():
    video_capture = cv2.VideoCapture(0)  # Change the argument to the file path if you want to process a video file
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Convert the OpenCV BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the RGB frame to PIL Image format
        pil_image = Image.fromarray(rgb_frame)

        # Perform object detection
        global model
        results = model(pil_image)

        # Process the detection results
        image_draw = ImageDraw.Draw(pil_image)

        for detection in results.xyxy[0]:
            xmin, ymin, xmax, ymax, conf, cls = detection.tolist()
            label = results.names[int(cls)]
            color = (255, 0, 0)  # Default color is red

            # Assign different colors based on class label
            if int(cls) == 0:
                color = (255, 0, 0)  # Red
            elif int(cls) == 1:
                color = (255, 165, 0)  # Orange
            elif int(cls) == 2:
                color = (255, 255, 0)  # Yellow
            elif int(cls) == 3:
                color = (0, 0, 255)  # Blue
            elif int(cls) == 4:
                color = (0, 0, 0)  # Black
            elif int(cls) == 5:
                color = (128, 0, 128)  # Purple
            elif int(cls) == 6:
                color = (255, 255, 255)  # White
            elif int(cls) == 7:
                color = (0, 255, 0)  # Green
            # Draw a rectangle on the frame
            image_draw.rectangle([(xmin, ymin), (xmax, ymax)], outline=color, width=2) # type: ignore
            image_draw.text((xmin, ymin), label, fill=color)
        # Convert the PIL Image back to OpenCV format for display
        opencv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
        # Display the resulting frame
        cv2.imshow('Real-time Object Detection', opencv_image)
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the windows
    video_capture.release()
    cv2.destroyAllWindows()

def import_image():
    global model
    global file_path
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)

    # Resize the image if needed
    image = image.resize((300, 300), Image.ANTIALIAS)

    # Convert the image to Tkinter-compatible format
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = Label(window, image=photo)
    image_label.image = photo  # type: ignore # Keep a reference to prevent garbage collection
    image_label.place(x = 70, y = 150)
    
def detect():
    image_original = Image.open(file_path)
    # Store the imported image
    imported_image = image_original
    # Inference
    results = model(imported_image)
    #draw
    draw = ImageDraw.Draw(imported_image)
    a = results.xyxy[0]  # im predictions (tensor)
    #Variable 
    tran = capSMD = resSMD = ic = capTH = diode = resTH = crys = 0
    coor = np.zeros((a.shape[0], a.shape[1] - 2), dtype=float)
    for i in range(a.shape[0]):
            for j in range(a.shape[1] - 2):
                coor[i][j] = float(a[i][j])
    # Draw square box with label
    for i in range(coor.shape[0]):
        xmin, ymin, xmax, ymax = coor[i][:4]  # Extract the coordinates for each box
        
        # Perform object detection only for selected components
        for component in selected_components:
            # Perform object detection for the selected component
            if component == "Transistor SMD":
                if int(a[i][5]) == 0:
                    draw.rectangle([(xmin, ymin), (xmax, ymax)], outline="red", width = 2) # type: ignore # type: ignore
                    tran = tran + 1
            if component == "Cap SMD":
                if int(a[i][5]) == 1:
                    draw.rectangle([(xmin, ymin), (xmax, ymax)], outline="orange", width = 2) # type: ignore
                    capSMD = capSMD + 1
               
            if component == "Res SMD":
                if int(a[i][5]) == 2:
                    draw.rectangle([(xmin, ymin), (xmax, ymax)], outline="yellow", width = 2) # type: ignore
                    resSMD = resSMD + 1

            if component == "IC":
                if int(a[i][5]) == 3:
                    draw.rectangle([(xmin, ymin), (xmax, ymax)], outline="blue", width = 2) # type: ignore
                    ic = ic + 1
                
            if component == "Cap Throughhole":
                if int(a[i][5]) == 4:
                    draw.rectangle([(xmin, ymin), (xmax, ymax)], outline="black", width = 2) # type: ignore
                    capTH = capTH + 1

            if component == "Crystal":
                if int(a[i][5]) == 5:
                    draw.rectangle([(xmin, ymin), (xmax, ymax)], outline="green", width = 2) # type: ignore
                    crys = crys + 1
                
            if component == "Diode":
                if int(a[i][5]) == 6:
                    draw.rectangle([(xmin, ymin), (xmax, ymax)], outline="white", width = 2) # type: ignore
                    diode = diode + 1
                    
            if component == "Res Throughhole":
                if int(a[i][5]) == 7:
                    draw.rectangle([(xmin, ymin), (xmax, ymax)], outline="pink", width = 2) # type: ignore
                    resTH = resTH + 1               
    # Resize the image if needed
    imported_image = imported_image.resize((300, 300), Image.ANTIALIAS)
    # Convert the image to Tkinter-compatible format
    photo = ImageTk.PhotoImage(imported_image)
    # Create a label to display the image
    detect_label = Label(window, image=photo)
    detect_label.image = photo  # type: ignore # Keep a reference to prevent garbage collection
    detect_label.place(x = 400, y = 150)
    # Update the component count labels
    tran_label.config(text = str(tran))
    capSMD_label.config(text=str(capSMD))
    resSMD_label.config(text=str(resSMD))
    ic_label.config(text=str(ic))
    crys_label.config(text=str(crys))
    capTH_label.config(text=str(capTH))
    resTH_label.config(text=str(resTH))
    diode_label.config(text=str(diode))

def Go_back():
    file_path = "D:/Project/Python/YoloV5/Main_window.py"
    subprocess.Popen(["python", file_path])
    window.destroy()

def remove_area():
    image_original = Image.open(file_path)
    imported_image = image_original
    # Inference
    results = model(imported_image)
    #draw
    draw = ImageDraw.Draw(imported_image)
    a = results.xyxy[0]  # im predictions (tensor)

    coor = np.zeros((a.shape[0], a.shape[1] - 2), dtype=float)
    for i in range(a.shape[0]):
            for j in range(a.shape[1] - 2):
                coor[i][j] = float(a[i][j])
    for i in range(coor.shape[0]):
        xmi, ymi, xma, yma = coor[i][:4]  # Extract the coordinates for each box
        xmin = int(xmi)
        xmax = int(xma)
        ymin = int(ymi)
        ymax = int(yma)
        if xmax > imported_image.size[0] - 1:
            xmax = imported_image.size[0] - 1
        if ymax > imported_image.size[1] - 1:
            ymax = imported_image.size[1] - 1
        # Perform object detection only for selected components
        for component in selected_components:
            # Perform object detection for the selected component
            if component == "Transistor SMD":
                if int(a[i][5]) == 0:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            imported_image.putpixel((m,n), (0, 255, 0))
            if component == "Cap SMD":
                if int(a[i][5]) == 1:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            imported_image.putpixel((m,n), (0, 255, 0))
                
            if component == "Res SMD":
                if int(a[i][5]) == 2:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            imported_image.putpixel((m,n), (0, 255, 0))

            if component == "IC":
                if int(a[i][5]) == 3:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            imported_image.putpixel((m,n), (0, 255, 0))
                
            if component == "Cap Throughhole":
                if int(a[i][5]) == 4:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            imported_image.putpixel((m,n), (0, 255, 0))

            if component == "Crystal":
                if int(a[i][5]) == 5:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            imported_image.putpixel((m,n), (0, 255, 0))
                
            if component == "Diode":
                if int(a[i][5]) == 6:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            imported_image.putpixel((m,n), (0, 255, 0))
                    
            if component == "Res Throughhole":
                if int(a[i][5]) == 7:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            imported_image.putpixel((m,n), (0, 255, 0))
                   
    # Resize the image if needed
    imported_image = imported_image.resize((300, 300), Image.ANTIALIAS)
    # Convert the image to Tkinter-compatible format
    photo = ImageTk.PhotoImage(imported_image)

    # Create a label to display the image
    detect_label = Label(window, image=photo)
    detect_label.image = photo  # type: ignore # Keep a reference to prevent garbage collection
    detect_label.place(x = 400, y = 150)

def keep_area():
    image_original = Image.open(file_path)
    save_image = image_original
    Image_Keep_Area = Image.new(save_image.mode, save_image.size)
    # Inference
    results = model(save_image)

    a = results.xyxy[0]  # im predictions (tensor)

    coor = np.zeros((a.shape[0], a.shape[1] - 2), dtype=float)
    for i in range(a.shape[0]):
            for j in range(a.shape[1] - 2):
                coor[i][j] = float(a[i][j])

    # Draw square box with label
    for i in range(coor.shape[0]):
        xmi, ymi, xma, yma = coor[i][:4]  # Extract the coordinates for each box
        xmin = int(xmi)
        xmax = int(xma)
        ymin = int(ymi)
        ymax = int(yma)
        if xmax > Image_Keep_Area.size[0] - 1:
            xmax = Image_Keep_Area.size[0] - 1
        if ymax > Image_Keep_Area.size[1] - 1:
            ymax = Image_Keep_Area.size[1] - 1

        # Perform object detection only for selected components
        for component in selected_components:
            # Perform object detection for the selected component
            if component == "Transistor SMD":
                if int(a[i][5]) == 0:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            R,G,B = save_image.getpixel((m,n))
                            Image_Keep_Area.putpixel((m,n), (np.uint8(B), np.uint8(G), np.uint8(R))) # type: ignore
            if component == "Cap SMD":
                if int(a[i][5]) == 1:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            R,G,B = save_image.getpixel((m,n))
                            Image_Keep_Area.putpixel((m,n), (np.uint8(B), np.uint8(G), np.uint8(R))) # type: ignore
                
            if component == "Res SMD":
                if int(a[i][5]) == 2:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            R,G,B = save_image.getpixel((m,n))
                            Image_Keep_Area.putpixel((m,n), (np.uint8(B), np.uint8(G), np.uint8(R))) # type: ignore

            if component == "IC":
                if int(a[i][5]) == 3:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            R,G,B = save_image.getpixel((m,n))
                            Image_Keep_Area.putpixel((m,n), (np.uint8(B), np.uint8(G), np.uint8(R))) # type: ignore
                
            if component == "Cap Throughhole":
                if int(a[i][5]) == 4:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            R,G,B = save_image.getpixel((m,n))
                            Image_Keep_Area.putpixel((m,n), (np.uint8(B), np.uint8(G), np.uint8(R))) # type: ignore

            if component == "Crystal":
                if int(a[i][5]) == 5:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            R,G,B = save_image.getpixel((m,n))
                            Image_Keep_Area.putpixel((m,n), (np.uint8(B), np.uint8(G), np.uint8(R))) # type: ignore
                
            if component == "Diode":
                if int(a[i][5]) == 6:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            R,G,B = save_image.getpixel((m,n))
                            Image_Keep_Area.putpixel((m,n), (np.uint8(B), np.uint8(G), np.uint8(R))) # type: ignore
                    
            if component == "Res Throughhole":
                if int(a[i][5]) == 7:
                    for m in range(xmin, xmax + 1):
                        for n in range(ymin, ymax + 1):
                            R,G,B = save_image.getpixel((m,n))
                            Image_Keep_Area.putpixel((m,n), (np.uint8(B), np.uint8(G), np.uint8(R))) # type: ignore
                   
    # Resize the image if needed
    Image_Keep_Area = Image_Keep_Area.resize((300, 300), Image.ANTIALIAS)
    # Convert the image to Tkinter-compatible format
    photo = ImageTk.PhotoImage(Image_Keep_Area)

    # Create a label to display the image
    detect_label = Label(window, image=photo)
    detect_label.image = photo  # type: ignore # Keep a reference to prevent garbage collection
    detect_label.place(x = 400, y = 150)

    
def exit_app():
    window.destroy()

window = Tk()
window.title("Hệ thống hỗ trợ nhận dạng và kiểm đếm số lượng linh kiện điện tử trên bo mạch")

# Set the window size
window.geometry("1050x600")


# Create checkboxes for each component
checkbox_vars = []
for i, label in enumerate(component_labels):
    var = IntVar()
    checkbox_vars.append(var)
    checkbox = Checkbutton(window, text=label, variable=var, command=lambda i=i, var=var: checkbox_changed(i, var))
    checkbox.place(x = 800, y = 100 + i*30)

import_button = Button(window, text="IMPORT IMAGE",font = ("Arial", 11, "bold"), command=import_image, bg="blue", fg="white", width= 15, height=2)
import_button.place(x = 250, y = 500)

# Button for detecting disease
detect_button = Button(window, text="DETECT",font = ("Arial", 11, "bold"), command=detect, bg="blue", fg="white", width= 15, height=2)
detect_button.place(x = 450, y = 500)

# Button for detecting disease
model_button = Button(window, text="LOAD MODEL",font = ("Arial", 11, "bold"), command=load_model, bg="red", fg="white", width= 15, height=2)
model_button.place(x = 50, y = 500)

# Button for exiting the app
exit_button = Button(window, text="EXIT",font = ("Arial", 11, "bold"), command=exit_app, bg="blue", fg="white", width= 15, height=2)
exit_button.place(x = 850, y = 500)

# Create a button to start the detection
start_button = Button(window, text="OPEN CAMERA", font = ("Arial", 11, "bold"), command=start_detection, bg="blue", fg="white", width= 15, height=2)
start_button.place(x = 650, y = 500)


# Button for remove area
exit_button = Button(window, text="Remove Area",font = ("Arial", 7, "bold"), command=remove_area, bg="green", fg="white", width= 9, height=2)
exit_button.place(x = 800, y = 370)

# Button for keep area
exit_button = Button(window, text="Keep Area",font = ("Arial", 7, "bold"), command=keep_area, bg="red", fg="white", width= 9, height=2)
exit_button.place(x = 900, y = 370)

# Button Sharpening
exit_button = Button(window, text="Go Back",font = ("Arial", 7, "bold"), command=Go_back, bg="red", fg="white", width= 15, height=2)
exit_button.place(x = 830, y = 420)

# Create a label for the tittle
tittle_label = Label(window, text="Hệ thống hỗ trợ nhận dạng và kiểm đếm số lượng linh kiện điện tử trên bo mạch",
                      font = ("Times New Roman", 20, "bold", ), fg = "black")
tittle_label.place(x = 80, y = 30)

# Create a label for displaying the predicted class
class_label = Label(window)
class_label.place(x = 300, y = 150)

#Create instruction lable
instruction_label = Label(window, text="", font=("Comic Sans MS", 13))
instruction_label.place(x=20, y=430)

# Create labels to display component counts
tran_label = Label(window, text = "0")
capSMD_label = Label(window, text="0")
resSMD_label = Label(window, text="0")
ic_label = Label(window, text="0")
capTH_label = Label(window, text="0")
resTH_label = Label(window, text="0")
diode_label = Label(window, text="0")
crys_label = Label(window, text="0")
# Add labels for other components

# Place the labels in the window
tran_label.place(x = 950, y = 100)
capSMD_label.place(x = 950, y = 130)
resSMD_label.place(x = 950, y = 160)
ic_label.place(x = 950, y = 190)
capTH_label.place(x = 950, y = 220)
crys_label.place(x = 950, y = 250)
diode_label.place(x=950, y=280)
resTH_label.place(x=950, y=310)
    #checkbox.place(x = 800, y = 100 + i*30)

window.mainloop()

