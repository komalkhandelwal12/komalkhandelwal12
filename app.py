import pickle
import pandas as pd
d=pickle.load(open('knn_classifier.pkl','rb'))
x_train=pickle.load(open('training_data.pkl','rb'))
import tkinter as tk

root=tk.Tk()
root.iconbitmap('c:/Users/pc/Downloads/fertilize.ico')

image_photo=None
def display():
    global image_photo

    input_data={
        'Temparature':int(e1.get()),
        'Humidity':int(e2.get()),
        'Moisture':int(e3.get()),
        'Soil Type': int(soil_type.index(dropdown1.get())),
        'Crop Type':int(crop_type.index(dropdown2.get())),
        'Nitrogen':int(e6.get()),
        'Potassium':int(e7.get()),
        'Phosphorous':int(e8.get()),

    }

    input_df=pd.DataFrame([input_data],columns=train.columns)
    ans=d.predict(input_df)
    if ans[0]==0:
        image_path="d:/Project/Fertilizer recommendation system/image/one.png"
    elif ans[0]==1:
        image_path="d:/Project/Fertilizer recommendation system/image/two.png"
    elif ans[0]==2:
        image_path="d:/Project/Fertilizer recommendation system/image/three.png"
    elif ans[0]==3:
        image_path="d:/Project/Fertilizer recommendation system/image/four.png"
    elif ans[0]==4:
        image_path="d:/Project/Fertilizer recommendation system/image/five.png"
    elif ans[0]==5:
        image_path="d:/Project/Fertilizer recommendation system/image/six.png"
    else:
        image_path="d:/Project/Fertilizer recommendation system/image/seven.png"

    image=Image.open(image_path)
    image_photo=ImageTk.PhotoImage(image)

image_label=tk.Label(root)
image.label.grid(row=12,column=1,padx=10,pady=10)

root.title("Fertilizer recommendation system App by Randhir")
root.iconbitmap("c:/Users/pc/Downloads/fertilize.ico")
l1=tk.Label(root,text="Enter Temparature")
l2=tk.Label(root,text="Enter Humadity")
l3=tk.Label(root,text="Enter Moisture")
l4=tk.Label(root,text="Enter Soil Type")
l5=tk.Label(root,text="Enter Crop Type")
l6=tk.Label(root,text="Enter Nitrogen")
l7=tk.Label(root,text="Enter Potassium")
l8=tk.Label(root,text="Enter Phosphorous")

e1=tk.Enter(root)
e2=tk.Enter(root)
e3=tk.Enter(root)

soil_type=["Sandy","Loamy","Black","Red","Clayey"]

selected_option=tk.Combobox(root,textvariable=selected_option,values=soil_type)
crop_type=["Maize","Sugarcane","Black","Cotton","Tobaccp","Paddy","Barley","Wheat","Millets","Oil seeds","Pulses","Ground Nuts"]
selected_option=tk.Combobox(root,textvariable=selected_options,values=crop_type)
e6=tk.Entry()
e7=tk.Entry()
e8=tk.Entry()

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
l4.grid(row=3,column=0)
l5.grid(row=4,column=0)
l6.grid(row=5,column=0)
l7.grid(row=6,column=0)
l8.grid(row=7,column=0)

e1.grid(row=0,coolumn=1)
e2.grid(row=1,coolumn=1)
e3.grid(row=2,coolumn=1)
dropdown1.grid(row=6,column=1)
dropdown2.grid(row=7,column=1)
e6.grid(row=2,coolumn=1)
e7.grid(row=2,coolumn=1)
e8.grid(row=2,coolumn=1)



root.mainloop()