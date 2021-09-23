from tkinter import *

import requests

proxies = { "http://": "1.186.40.177:80",
           "https://": "1.186.40.177:80"
}
r = requests.get("https://google.com/", proxies=proxies)

def VPN():
    print (r.status_code) #r.reasonSS


window=Tk()


window.title('Hello Python')
btn=Button(window, text="start", fg='blue', command = VPN)
btn.place(x=80, y=100)
window.geometry("300x200+10+20")
window.mainloop()