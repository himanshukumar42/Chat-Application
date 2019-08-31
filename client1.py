from tkinter import *
import socket
class Gui:
    def __init__(self,master):
        self.f1 = Frame(master)
        self.t1 = Text(self.f1,font=("times new roman",13,"bold"),width=73,height=20,borderwidth=6,relief=GROOVE)
        self.t1.grid(row=0,column=0)
        self.f1.grid(row=0,column=0,padx=10,pady=6)
        
        self.f2 = Frame(master)
        self.l1 = Label(self.f2, text="Message",bg="lightblue",font="Arial 10 bold")
        self.l1.grid(row=0,column=0)
        self.msg=StringVar()
        self.e1 = Entry(self.f2,textvariable=self.msg)
        self.e1.grid(row=0,column=1,ipadx=100,ipady=10,padx=9,pady=9)
        self.b1 = Button(self.f2, text="Send",width=8,padx=8,pady=5,bg="blue",fg="white",font=("Arial",10,"bold"),command=self.message)
        master.bind("<Return>",self.message)
        self.b1.grid(row=0,column=2,sticky=W)
        self.f2.config(bg="lightblue")
        self.f2.grid(row=1,column=0)
    def message(self,event=None):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 7777
        client_socket.connect((host,port))
        cmsg = self.e1.get()
        client_socket.send(cmsg.encode())
        smsg = client_socket.recv(1024).decode()
        self.t1.insert(END, "Server : {} \n".format(smsg))
        self.t1.insert(END, "You : {} \n".format(cmsg))
        self.msg.set("")
root = Tk()
b1 = Gui(root)
root.title("Client")
root.iconbitmap("msg.ico")
root.config(bg="lightblue")
root.resizable(0,0)
root.mainloop()
