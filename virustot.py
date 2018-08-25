#--coding:utf-8-*-
import requests
import json
from Tkinter import *
import Tkinter ,tkFileDialog
from threading import Thread
import time 
def dos_ad(text):
    text2 = ""
    text = text[::-1]
    for i in text:
        if (i != "/"): 
            text2 = text2 + i
        else:
            break
    return text2
def sec():
    pencere.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes =(("all files","*.*"),("jpeg files","*.jpg")))
    global path
    path = pencere.filename
    print path
    try:
        
        dosya_label['text'] = "---Seçildi---"
    except:
        dosya_label['text'] = "Hata oluştu"

def calistir_f():
    hos_label['text'] = "...Taranıyor..."
    

    def calis():
        fir = time.time()
        key = '632117c49009620b3ef099b1bf3d78f89223cb5fb26cdde4eb53df971dd48623'
        params = {'apikey': key}
        file_name = dos_ad(path)
        files = {'file': (file_name, open(path, 'rb'))}
        response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
        response2 = response.json()

        has = response2['resource']

        params = {'apikey': key, 'resource': has}
        headers = {
          "Accept-Encoding": "gzip, deflate",
          "User-Agent" : "gzip,  My Python requests library example client or username"
          }
        response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
        params=params, headers=headers)
        response3 = response.json()
        
        a = 0
        for i,j in response3['scans'].iteritems():
       
            if j['detected'] == True:
                sonuc_ekran.insert(INSERT,"[+]" + i + " detected something !!!"+'\n')
                a += 1
            else:
                continue
        if (a == 0):
             b = time.time()
             sonuc_ekran.insert(INSERT,"Nothing detected. \n It took second {}".format(int(b-fir)))
        hos_label['text'] = "Tarama bitti"
        
    t1 = Thread(target = calis)
    t1.start()
    
        
pencere = Tk()
pencere.title("Alparslan AntiNotVirus v0.1 Bafra Fen Lisesi '21")
pencere.geometry("600x400+480+320")
pencere.configure(background = "midnight blue")
pencere.resizable(width = False,height = False)

hos_label = Label(text = "Hoş geldiniz",fg = "green",bg = "black",font = "Verdana 13 bold")
hos_label.pack(fill = BOTH)

dosya_label = Label(text = "Butona tıkla ",fg = "turquoise",bg = "dark green",font = "Verdana 8 bold")
dosya_label.place(relx = "0.02",rely = "0.17")

dosya_buton = Button(pencere,text = "Taranacak dosya seç ",command = sec,fg = "yellow",bg = "dark green")
dosya_buton.place(relx = "0.18",rely = "0.15",relheight = "0.1",relwidth = "0.2")

calistir = Button(pencere,text = "Calistir",bg = "lime green",fg = "goldenrod1",command = calistir_f)
calistir.place(relx = "0.18",rely = "0.4",relheight = "0.1",relwidth = "0.2")
pencere.bind("<Return>",calistir_f)


calis_lab = Label(text = "Tıkla",fg = "gray13",bg = "lime green",font = "Verdana 8 bold",activeforeground = "red4",activebackground= "cyan4")
calis_lab.place(relx = "0.02",rely = "0.43",relwidth = "0.14")

sonuc_ekran = Text(pencere,bg ="snow", fg = "DarkOrange4" )
sonuc_ekran.place(relx = " 0.5",rely= "0.14",relheight = "0.8",relwidth = "0.45")

pencere.mainloop()
        
    
