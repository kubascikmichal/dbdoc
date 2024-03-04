from bluetooth import discover_devices
from tkinter import CENTER, SW, Frame,Button,OptionMenu,Label,StringVar,Entry,Tk
import socket
import json
from time import sleep

class App():
    def __init__(self, parent):
        self.socket = 0

        #root config
        self.parent = parent
        self.parent.title("Generator configurator")
        self.parent.config(bg='blue')
        self.parent.protocol("WM_DELETE_WINDOW", self.clear)

        #basic root layout
        self.top_frame = Frame(self.parent, width=800, height=40)
        self.top_frame.grid(row=0, column=0)
        self.top_frame.config(bg="blue")
        self.app_frame = Frame(self.parent, width=1600, height=800)
        self.app_frame.grid(row=1, column=0)
        self.app_frame.config(bg="blue")

        #app layout
        self.info_label = Label(self.top_frame, text="Welcome!")
        self.info_label.config(bg='blue')
        self.info_label.grid(row=0, column=0)
        self.options = [""]
        self.nearby_devices = []
        self.clicked = StringVar()
        self.clicked.set("Reload first") 
        self.devices_frame = Frame(self.app_frame, width=800, height=800)
        self.devices_frame.grid(row=0, column=0)
        self.devices_frame.config(bg='blue')
        self.config_frame = Frame(self.app_frame, width=800, height=800)
        self.config_frame.grid(row=0, column=1)
        self.config_frame.config(bg='blue')

        #device config layout
        self.drop = OptionMenu(self.devices_frame, self.clicked, *self.options)
        self.drop.grid(row=0, column=0, padx=10, pady=5)
        self.drop.config(bg='light blue')
        self.reload_button = Button( self.devices_frame, text = "Reload" , command = self.refresh )
        self.reload_button.grid(row=1, column=0, padx=10, pady=5)
        self.reload_button.config(bg='light blue')
        self.connect_button = Button( self.devices_frame, text = "Connect" , command = self.connect )
        self.connect_button.grid(row=2, column=0, padx=10, pady=5)
        self.connect_button.config(bg='light blue')
        self.disconnect_button = Button( self.devices_frame, text = "Disconnect" , command = self.disconnect )
        self.disconnect_button.grid(row=3, column=0, padx=10, pady=5)
        self.disconnect_button.config(bg='light blue')
        
        #config frame
        self.time_label = Label(self.config_frame, text="Time interval")
        self.time_label.grid(row=0, column=0)
        self.time_label.config(bg='blue')
        self.time_entry = Entry(self.config_frame)
        self.time_entry.grid(row=1,column=0)
        self.delay_label = Label(self.config_frame, text="Time delay")
        self.delay_label.grid(row=2, column=0)
        self.delay_label.config(bg='blue')
        self.delay_entry = Entry(self.config_frame)
        self.delay_entry.grid(row=3,column=0)
        self.min_freq_label = Label(self.config_frame, text="Minimum frequency")
        self.min_freq_label.grid(row=4, column=0)
        self.min_freq_label.config(bg='blue')
        self.min_freq_entry = Entry(self.config_frame)
        self.min_freq_entry.grid(row=5,column=0)
        self.max_freq_label = Label(self.config_frame, text="Maximum frequency")
        self.max_freq_label.grid(row=6, column=0)
        self.max_freq_label.config(bg='blue')
        self.max_freq_entry = Entry(self.config_frame)
        self.max_freq_entry.grid(row=7 ,column=0)
        self.step_size_label = Label(self.config_frame, text="Step size")
        self.step_size_label.grid(row=8, column=0)
        self.step_size_label.config(bg='blue')
        self.step_size_entry = Entry(self.config_frame)
        self.step_size_entry.grid(row=9, column=0)
        self.bottom_frame = Frame(self.config_frame, width=800, height=800)
        self.bottom_frame.grid(row=10, column=0)
        self.send_data_button = Button( self.bottom_frame, text = "Set" , command = self.send_data )
        self.send_data_button.pack(side="left",  expand=1,fill='both')
        self.load_data_button = Button( self.bottom_frame, text = "Load" , command = self.load_data )
        self.load_data_button.pack(side="right",  expand=1,fill='both')


    def refresh(self):
        self.info_label.config(text="Reloading...")
        sleep(0.1)
        self.nearby_devices = discover_devices(lookup_names = True)
        menu =  self.drop["menu"]
        menu.delete(0, "end")
        for  addr,name in self.nearby_devices:
            menu.add_command(
                label = name,
                command=lambda
                value = name : self.clicked.set(value)
            )
        self.info_label.config(text="New devices founded!")

    def connect(self):
        self.info_label.config(text="Connecting...")
        self.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        channel = 1
        baddr = ''
        for  addr,name in self.nearby_devices:
            self.clicked
            if name == self.clicked.get():
                baddr = addr
                break
        print(self.clicked.get(), baddr)
        self.socket.connect((baddr,channel))
        self.info_label.config(text="Connected to "+self.clicked.get())
    
    def disconnect(self):
        self.socket.close()
        self.info_label.config(text="Disconnected")

    def send_data(self):
        list_config = {
            'time_interval':self.time_entry.get(),
            'delay':self.delay_entry.get(),
            'minimum_frequency':self.min_freq_entry.get(),
            'maximum_frequency':self.max_freq_entry.get(),
            'step_size':self.step_size_entry.get()
        }
        config = json.dumps(list_config)
        print(config)
        self.socket.send(bytes(str(config), 'ascii'))

    def load_data(self):
        self.socket.send(bytes(len("SendConfig")))
        self.socket.send(bytes("SendConfig", 'ascii'))
        answer = self.socket.recv(1024)
        print(answer)

    def clear(self):
        if(self.socket):
            self.socket.close()
        self.parent.destroy()
        self.parent.quit

root = Tk() 
App(root)
root.mainloop()
