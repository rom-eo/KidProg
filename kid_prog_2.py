#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# Welcome to KidProg!

## Goal

This simple program teaches the fundamental of programming to kids.

1. Devise an algorithm
2. Implement it by using language syntax.
 
## Task

Move the white box to the green box by writing a code.
The syntax is made of four words: left, right, up and down.
Each non empty line should have only one word.
"""
from tkinter import Tk,Button,Label,Text,messagebox
import random

class app:
    def ch(self):
        return random.choice(range(self.size))
    def __init__(self):
        self.instructions="""Hello Kid! Move the white box to the green box.
           Write "right" to move it right. Write "left" to move it left. 
           Write "up" to move it up. Write "down" to move it down.
           Go to a new line each time. Then click on "Execute".
        """
        self.size=5
        self.initPoints=[((2,2),(2,3)),((2,2),(2,1)),
                         ((2,2),(3,2)),((2,2),(1,2))]+\
                         [[[self.ch(),self.ch()],
                           [self.ch(),self.ch()]] for _ in range(20)]
        self.a1=self.a2=self.b1=self.b2=0
        self.top = Tk() 
        self.top.title("KidProg")
         
        self.gameLevel=0
        
        self.buttons=[ [Button(self.top, text = "   ",background = "pink",pady=10)
        for i in range(self.size)] for j in range(self.size)]
        
        for i in range(self.size):
            for j in range(self.size):
                self.buttons[i][j].grid(row = i, column = j, sticky = 'nwes')#, pady = 2)
        
        self.label=Label(self.top,text=self.instructions) 
        self.label.grid(row=self.size,columnspan=self.size)
        
        self.text=Text(self.top,height=10)
        self.text.grid(row=self.size+1,columnspan=self.size) 
        
        self.execBut=Button(self.top, text = "Execute",command=self.fun)#,background = "pink",pady=10)
        self.execBut.grid(row=self.size+2,columnspan=self.size)
        
        self.a1,self.b1,self.a2,self.b2=self.level(self.gameLevel)
        self.buttons[self.a1][self.b1]["background"]='white'
        self.buttons[self.a2][self.b2]["background"]='green'
        
        self.labelOutput=Label(self.top,text="") 
        self.labelOutput.grid(row=self.size+3,columnspan=self.size)
        
    def execute(self):
        self.top.mainloop() 


    def level(self,i):   
        return [xy  for x in self.initPoints[i] for xy in x]

  
    def fun(self):
        theText=self.text.get("1.0","end-1c")#, END)#"
        lines=theText.split("\n")
        
        for line in lines:
            
            if line=="right" and self.b1!=self.size-1:    
                self.buttons[self.a1][self.b1]['background']='pink'
                self.b1+=1
                #self.labelOutput['text']= self.labelOutput['text'] +str((self.a1,self.b1))+" "
                self.buttons[self.a1][self.b1]['background']='white'
                
            if line=="left" and self.b1!=0:
                self.buttons[self.a1][self.b1]['background']='pink'
                self.b1-= 1 
                #self.labelOutput['text']= self.labelOutput['text']+\
                #str((self.a1,self.b1))+" "    
                self.buttons[self.a1][self.b1]['background']='white'
                
            if line=="down" and self.a1!=self.size-1:
                self.buttons[self.a1][self.b1]['background']='pink'
                self.a1+=1                
                #self.labelOutput['text']= self.labelOutput['text'] +str((self.a1,self.b1))+' '
                self.buttons[self.a1][self.b1]['background']='white'
                
            if line=="up" and self.a1!=0:
                self.buttons[self.a1][self.b1]['background']='pink' 
                self.a1-=1
                #self.labelOutput['text']= self.labelOutput['text'] +str((self.a1,self.b1))+' '
                self.buttons[self.a1][self.b1]['background']='white'
                
        if self.a1==self.a2 and self.b1==self.b2:
            messagebox.showinfo("Congratulations!", "Well done Super Programmer!") 
            self.gameLevel+=1
            self.buttons[self.a1][self.b1]['background']='pink'
            self.a1,self.b1,self.a2,self.b2=self.level(self.gameLevel%len(self.initPoints))
            self.buttons[self.a1][self.b1]["background"]='white'
            self.buttons[self.a2][self.b2]["background"]='green'
   
Myapp=app()    
Myapp.execute()
 
