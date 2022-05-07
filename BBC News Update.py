import requests
import json
from tkinter import*

root=Tk()
root.title("BBC NEWS UPDATE")
root.geometry("900x600")

label=Label(root,text="BBC News Update",font=("times bold",18))
label.place(relx=0.5,rely=0.1,anchor=CENTER)

news1=Label(root,fg="red",font=("arial italic",14),wraplength=500)
news1.place(relx=0.05,rely=0.2,anchor=W)
news1_desc=Text(root,width=100,height=3,relief=FLAT)
news1_desc.place(relx=0.05,rely=0.28,anchor=W)

news2=Label(root,fg="red",font=("arial italic",14),wraplength=500)
news2.place(relx=0.05,rely=0.4,anchor=W)
news2_desc=Text(root,width=100,height=3,relief=FLAT)
news2_desc.place(relx=0.05,rely=0.48,anchor=W)

news3=Label(root,fg="red",font=("arial italic",14),wraplength=500)
news3.place(relx=0.05,rely=0.6,anchor=W)
news3_desc=Text(root,width=100,height=3,relief=FLAT)
news3_desc.place(relx=0.05,rely=0.68,anchor=W)

news4=Label(root,fg="red",font=("arial italic",14),wraplength=500)
news4.place(relx=0.05,rely=0.8,anchor=W)
news4_desc=Text(root,width=100,height=3,relief=FLAT)
news4_desc.place(relx=0.05,rely=0.88,anchor=W)

news1.destroy()
news2.destroy()
news3.destroy()
news4.destroy()
news1_desc.destroy()
news2_desc.destroy()
news3_desc.destroy()
news4_desc.destroy()
def Upload_News():
    global news1
    global news2
    global news3
    global news4
    global news1_desc
    global news2_desc
    global news3_desc
    global news4_desc
    
    news1.destroy()
    news2.destroy()
    news3.destroy()
    news4.destroy()
    news1_desc.destroy()
    news2_desc.destroy()
    news3_desc.destroy()
    news4_desc.destroy()
    
    label=Label(root,text="BBC News Update",font=("times bold",18))
    label.place(relx=0.5,rely=0.1,anchor=CENTER)

    news1=Label(root,fg="red",font=("arial italic",14),wraplength=500)
    news1.place(relx=0.05,rely=0.2,anchor=W)
    news1_desc=Text(root,width=100,height=3,relief=FLAT)
    news1_desc.place(relx=0.05,rely=0.28,anchor=W)

    news2=Label(root,fg="red",font=("arial italic",14),wraplength=500)
    news2.place(relx=0.05,rely=0.4,anchor=W)
    news2_desc=Text(root,width=100,height=3,relief=FLAT)
    news2_desc.place(relx=0.05,rely=0.48,anchor=W)

    news3=Label(root,fg="red",font=("arial italic",14),wraplength=500)
    news3.place(relx=0.05,rely=0.6,anchor=W)
    news3_desc=Text(root,width=100,height=3,relief=FLAT)
    news3_desc.place(relx=0.05,rely=0.68,anchor=W)

    news4=Label(root,fg="red",font=("arial italic",14),wraplength=500)
    news4.place(relx=0.05,rely=0.8,anchor=W)
    news4_desc=Text(root,width=100,height=3,relief=FLAT)
    news4_desc.place(relx=0.05,rely=0.88,anchor=W)

    
    news1_desc.config(state=NORMAL)
    news2_desc.config(state=NORMAL)
    news3_desc.config(state=NORMAL)
    news4_desc.config(state=NORMAL)
    
    api_key=requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey="+"f6ca0c4097d24b2093deab03608bab8b")
    api_output_json=json.loads(api_key.content)
    
    news_name_1=api_output_json["articles"][0]["title"]
    news_desc_1=api_output_json["articles"][0]["description"]
     
    news_name_2=api_output_json["articles"][1]["title"]
    news_desc_2=api_output_json["articles"][1]["description"]
    
    news_name_3=api_output_json["articles"][2]["title"]
    news_desc_3=api_output_json["articles"][2]["description"]
    
    news_name_4=api_output_json["articles"][3]["title"]
    news_desc_4=api_output_json["articles"][3]["description"]
    
    news1['text']="Title 1:"+news_name_1
    news1_desc.insert(END,"Description 1:"+news_desc_1)
    
    news2['text']="Title 2:"+news_name_2
    news2_desc.insert(END,"Description 2:"+news_desc_2)
    
    news3['text']="Title 3:"+news_name_3
    news3_desc.insert(END,"Description 3:"+news_desc_3)
    
    news4['text']="Title 4:"+news_name_4
    news4_desc.insert(END,"Description 4:"+news_desc_4)
    
    news1_desc.config(state=DISABLED)
    news2_desc.config(state=DISABLED)
    news3_desc.config(state=DISABLED)
    news4_desc.config(state=DISABLED)
    
    Reload.place(relx=0.5,rely=0.95,anchor=CENTER)
    
Reload=Button(root,text="Refresh ↻", command=Upload_News,relief=FLAT,bg="Aqua",fg="blue")
Reload.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()