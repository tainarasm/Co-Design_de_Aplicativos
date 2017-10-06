import serial
import time

from tkinter import Tk, Frame


def up(event):
	ser.write(b'q')

def down(event):
	ser.write(b'a')

def left(event):
	ser.write(b'w')

def right(event):
	ser.write(b's')

def f(event):
	ser.write(b'f')

def insert(event):
	ser.write(b'g')

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/cu.usbmodem1411'
ser.open()
time.sleep(1.8)

root = Tk()
root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<f>", f )
root.bind("<g>", insert)

frame = Frame(root, width=100, height=100)
frame.pack()

root.mainloop()

ser.close()

"""
x=0

"""
