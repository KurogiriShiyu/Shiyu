import tkinter as tk 
from tkinter.scrolledtext import ScrolledText
from pygame import mixer
import random
import yaml

class ButtonPro(tk.Button):
    def __init__(self,family,name,point,master=None,cnf={},**kw):
        tk.Button.__init__(self,master,cnf,**kw)
        self.family = family
        self.name = name
        self.point = point


class YamlSystem:
    def __init__(self):
        pass
    
    def append_date(self,move_memory,delete_memory):
        with open("メモ0.yaml", "w") as yf:
            yaml.dump({"Frist":{
                "move_memory": move_memory,
                "delete_memory": delete_memory
            }
            }, yf, default_flow_style=False)

    def load_move_memory(self):
        with open("メモ0.yaml") as file:
            self.yamldata = yaml.safe_load(file)
        return(self.yamldata['Frist']['move_memory'])
    
    def load_delete_memory(self):
        with open("メモ0.yaml") as file:
            self.yamldata = yaml.safe_load(file)
        return(self.yamldata['Frist']['delete_memory'])



class Chess:
    def __init__(self,stage):
        self.yml = YamlSystem()
        self.stage = stage
        canvas_main = tk.Canvas(self.stage, width = 900, height = 551)
        self.canvas_main = canvas_main
        canvas_main.place(x=0,y=0)
        canvas_sub = tk.Canvas(self.stage,width = 900, height = 551)
        self.canvas_sub = canvas_sub
        finish_canvas = tk.Canvas(self.stage,width = 900, height = 551)
        self.finish_canvas = finish_canvas
        self.hold_piece = None
        self.marks = []
        self.turn = True
        self.move_memory = []
        self.delete_memory = []
        self.automatic_swich = False
        self.sound_swich = False
        self.sound_donlord()

    def donlord(self):
        DBishop = {'img': tk.PhotoImage(file="Photo.py/DBishop.png"),'point':{'x':[175,325],'y':[75]}}
        DPorn = {'img': tk.PhotoImage(file="Photo.py/DPorn.png"),'point':{'x':[75,125,175,225,275,325,375,425],'y':[125]}}
        DKing = {'img': tk.PhotoImage(file="Photo.py/DKing.png"),'point':{'x':[275],'y':[75]}}
        DNight = {'img': tk.PhotoImage(file="Photo.py/DNight.png"),'point':{'x':[125,375],'y':[75]}}
        DQueen = {'img': tk.PhotoImage(file="Photo.py/DQueen.png"),'point':{'x':[225],'y':[75]}}
        DRook = {'img': tk.PhotoImage(file="Photo.py/DRook.png"),'point':{'x':[75,425],'y':[75]}}
        WBishop = {'img': tk.PhotoImage(file="Photo.py/WBishop.png"),'point':{'x':[175,325],'y':[425]}}
        WPorn = {'img': tk.PhotoImage(file="Photo.py/WPorn.png"),'point':{'x':[75,125,175,225,275,325,375,425],'y':[375]}}
        WKing = {'img': tk.PhotoImage(file="Photo.py/WKing.png"),'point':{'x':[275],'y':[425]}}
        WNight = {'img': tk.PhotoImage(file="Photo.py/WNight.png"),'point':{'x':[125,375],'y':[425]}}
        WQueen = {'img': tk.PhotoImage(file="Photo.py/WQueen.png"),'point':{'x':[225],'y':[425]}}
        WRook = {'img': tk.PhotoImage(file="Photo.py/WRook.png"),'point':{'x':[75,425],'y':[425]}}
        self.pieces = [DBishop,DPorn,DKing,DNight,DQueen,DRook,WBishop,WPorn,WKing,WNight,WQueen,WRook]

    def check(self,x,y,kind,s='ON'):
        if 1<=x and x<=8 and 1<=y and y<=8:
            tag = self.canvas_sub.find_closest(x*50+25,y*50+25)[0]
            if 75<=tag and tag<=106:
                if kind == 'O'and 75<=tag and tag<=106:
                    if s == 'ON':
                        return(True)
                    if s == 'OFF':
                        return(False)
                elif kind == 'D'and 75<=tag and tag<=90:
                    return(True)
                elif kind == 'W'and 91<=tag and tag<=106:
                    return(True)
                else:
                    return(False)
            else:
                if s == 'ON':
                        return(False)
                if s == 'OFF':
                        return(True)
        else:
            return(False)


    def DR_move(self,X,Y):
        point = [-1,1]
        for j in point:
            x=X
            y=Y
            while self.check(x+j,y,'W','OFF'):
                if self.check(x+j,y,'W'):
                    x = x+j
                    tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     
                    break
                x = x+j
                tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                self.marks.append(tag)
                 
        for j in point:
            x=X
            y=Y
            while self.check(x,y+j,'W','OFF'):
                if self.check(x,y+j,'W'):
                    y = y+j
                    tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     
                    break
                y = y+j
                tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                self.marks.append(tag)
                 

    def DN_move(self,x,y):
        points1 = [-2,2]
        points2 = [-1,1]
        for i in points1:
            for j in points2:
                if self.check(x+i,y+j,'W','OFF'):
                    tag = self.canvas_sub.create_oval((x+i)*50+15,(y+j)*50+15,(x+i)*50+35,(y+j)*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     
        for i in points2:
            for j in points1:
                if self.check(x+i,y+j,'W','OFF'):
                    tag = self.canvas_sub.create_oval((x+i)*50+15,(y+j)*50+15,(x+i)*50+35,(y+j)*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     

    def DB_move(self,X,Y):
        point = [-1,1]
        for j in point:
            for i in point:
                x=X
                y=Y
                while self.check(x+j,y+i,'W','OFF'):
                    if self.check(x+j,y+i,'W'):
                        x = x+j
                        y = y+i
                        tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                        self.marks.append(tag)
                         
                        break
                    x = x+j
                    y = y+i
                    tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     

    def DQ_move(self,X,Y):
        point = [-1,1]
        for j in point:
            for i in point:
                x=X
                y=Y
                while self.check(x+j,y+i,'W','OFF'):
                    if self.check(x+j,y+i,'W'):
                        x = x+j
                        y = y+i
                        tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                        self.marks.append(tag)
                         
                        break
                    x = x+j
                    y = y+i
                    tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     
        for j in point:
            x=X
            y=Y
            while self.check(x+j,y,'W','OFF'):
                if self.check(x+j,y,'W'):
                    x = x+j
                    tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     
                    break
                x = x+j
                tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                self.marks.append(tag)
                 
        for j in point:
            x=X
            y=Y
            while self.check(x,y+j,'W','OFF'):
                if self.check(x,y+j,'W'):
                    y = y+j
                    tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     
                    break
                y = y+j
                tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                self.marks.append(tag)
                 

    def DK_move(self,x,y):
        points = [-1,0,1]
        for i in points:
            for j in points:
                if self.check(x+i,y+j,'W','OFF'):
                    tag = self.canvas_sub.create_oval((x+i)*50+15,(y+j)*50+15,(x+i)*50+35,(y+j)*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     

    def DP_move(self,x,y):
        if self.check(x,y+1,'O','OFF'):
            tag = self.canvas_sub.create_oval(x*50+15,(y+1)*50+15,x*50+35,(y+1)*50+35,fill="#00AA00")
            self.marks.append(tag)
             
        if y == 2:
            if self.check(x,y+2,'O','OFF'):
                tag = self.canvas_sub.create_oval(x*50+15,(y+2)*50+15,x*50+35,(y+2)*50+35,fill="#00AA00")
                self.marks.append(tag)
                 
        if self.check(x+1,y+1,'W'):
            tag = self.canvas_sub.create_oval((x+1)*50+15,(y+1)*50+15,(x+1)*50+35,(y+1)*50+35,fill="#00AA00")
            self.marks.append(tag)
             
        if self.check(x-1,y+1,'W'):
            tag = self.canvas_sub.create_oval((x-1)*50+15,(y+1)*50+15,(x-1)*50+35,(y+1)*50+35,fill="#00AA00")
            self.marks.append(tag)
             

    def WR_move(self,X,Y):
        point = [-1,1]
        for j in point:
            x=X
            y=Y
            while self.check(x+j,y,'D','OFF'):
                if self.check(x+j,y,'D'):
                    x = x+j
                    tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     
                    break
                x = x+j
                tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                self.marks.append(tag)
                 
        for j in point:
            x=X
            y=Y
            while self.check(x,y+j,'D','OFF'):
                if self.check(x,y+j,'D'):
                    y = y+j
                    tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     
                    break
                y = y+j
                tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                self.marks.append(tag)
                 

    def WN_move(self,x,y):
        points1 = [-2,2]
        points2 = [-1,1]
        for i in points1:
            for j in points2:
                if self.check(x+i,y+j,'D','OFF'):
                    tag = self.canvas_sub.create_oval((x+i)*50+15,(y+j)*50+15,(x+i)*50+35,(y+j)*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     
        for i in points2:
            for j in points1:
                if self.check(x+i,y+j,'D','OFF'):
                    tag = self.canvas_sub.create_oval((x+i)*50+15,(y+j)*50+15,(x+i)*50+35,(y+j)*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     

    def WB_move(self,X,Y):
        point = [-1,1]
        for j in point:
            for i in point:
                x=X
                y=Y
                while self.check(x+j,y+i,'D','OFF'):
                    if self.check(x+j,y+i,'D'):
                        x = x+j
                        y = y+i
                        tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                        self.marks.append(tag)
                         
                        break
                    x = x+j
                    y = y+i
                    tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     

    def WQ_move(self,X,Y):
        point = [-1,1]
        for j in point:
            for i in point:
                x=X
                y=Y
                while self.check(x+j,y+i,'D','OFF'):
                    if self.check(x+j,y+i,'D'):
                        x = x+j
                        y = y+i
                        tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                        self.marks.append(tag)
                         
                        break
                    x = x+j
                    y = y+i
                    tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     
        for j in point:
            x=X
            y=Y
            while self.check(x+j,y,'D','OFF'):
                if self.check(x+j,y,'D'):
                    x = x+j
                    tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     
                    break
                x = x+j
                tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                self.marks.append(tag)
                 
        for j in point:
            x=X
            y=Y
            while self.check(x,y+j,'D','OFF'):
                if self.check(x,y+j,'D'):
                    y = y+j
                    tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     
                    break
                y = y+j
                tag = self.canvas_sub.create_oval(x*50+15,y*50+15,x*50+35,y*50+35,fill="#00AA00")
                self.marks.append(tag)
                 

    def WK_move(self,x,y):
        points = [-1,0,1]
        for i in points:
            for j in points:
                if self.check(x+i,y+j,'D','OFF'):
                    tag = self.canvas_sub.create_oval((x+i)*50+15,(y+j)*50+15,(x+i)*50+35,(y+j)*50+35,fill="#00AA00")
                    self.marks.append(tag)
                     

    def WP_move(self,x,y):
        if self.check(x,y-1,'O','OFF'):
            tag = self.canvas_sub.create_oval(x*50+15,(y-1)*50+15,x*50+35,(y-1)*50+35,fill="#00AA00")
            self.marks.append(tag)
             
        if y == 7:
            if self.check(x,y-2,'O','OFF'):
                tag = self.canvas_sub.create_oval(x*50+15,(y-2)*50+15,x*50+35,(y-2)*50+35,fill="#00AA00")
                self.marks.append(tag)
                 
        if self.check(x+1,y-1,'D'):
            tag = self.canvas_sub.create_oval((x+1)*50+15,(y-1)*50+15,(x+1)*50+35,(y-1)*50+35,fill="#00AA00")
            self.marks.append(tag)
             
        if self.check(x-1,y-1,'D'):
            tag = self.canvas_sub.create_oval((x-1)*50+15,(y-1)*50+15,(x-1)*50+35,(y-1)*50+35,fill="#00AA00")
            self.marks.append(tag)
             


    def piece_move(self,tag,x,y):
        x = x//50
        y = y//50
        if 75<=tag and tag<=106:
            self.hold_piece = [tag,x,y]
            for i in self.marks:
                self.canvas_sub.delete(i)
            if 77<=tag and tag<=84:
                self.DP_move(x,y)
            elif tag == 89 or tag == 90:
                self.DR_move(x,y)
            elif tag == 86 or tag == 87:
                self.DN_move(x,y)
            elif tag == 75 or tag == 76:
                self.DB_move(x,y)
            elif tag == 88:
                self.DQ_move(x,y)
            elif tag == 85:
                self.DK_move(x,y)
            elif 93<=tag and tag<=100:
                self.WP_move(x,y)
            elif tag == 105 or tag == 106:
                self.WR_move(x,y)
            elif tag == 102 or tag == 103:
                self.WN_move(x,y)
            elif tag == 91 or tag == 92:
                self.WB_move(x,y)
            elif tag == 104:
                self.WQ_move(x,y)
            elif tag == 101:
                self.WK_move(x,y)
            else:
                pass
        elif tag >= 107 and self.hold_piece != None:
            self.move_log(x,y)
            for i in self.marks:
                self.canvas_sub.delete(i)
            self.marks = []
            tag = self.canvas_sub.find_closest(x*50+25, y*50+25)[0]
            if 75<=tag and tag<=106:
                self.delete_memory.append([x,y,tag])
                self.delete_move(tag)
                x = x-self.hold_piece[1]
                y = y-self.hold_piece[2]
                self.canvas_sub.move(self.hold_piece[0],x*50,y*50)
                self.move_memory.append([x,y,self.hold_piece[0],True])
                self.hold_piece = None
                self.sounds('attack')
            else:
                x = x-self.hold_piece[1]
                y = y-self.hold_piece[2]
                self.canvas_sub.move(self.hold_piece[0],x*50,y*50)
                self.move_memory.append([x,y,self.hold_piece[0],False])
                self.hold_piece = None
                self.sounds('move')
            self.turn_change()
        else:
            pass

    def delete_move(self,tag):
        z = len(self.delete_memory)
        if z<=8:
            self.canvas_sub.moveto(tag,z*50+450,300)
        elif 9<=z and z<=16:
            self.canvas_sub.moveto(tag,(z-8)*50+450,350)
        elif 17<=z and z<=24:
            self.canvas_sub.moveto(tag,(z-16)*50+450,400)
        elif 25<=z and z<=32:
            self.canvas_sub.moveto(tag,(z-24)*50+450,450)
        self.finish(tag)

    def finish(self,tag):
        if tag == 101 or tag == 85:
            self.change_frame(self.canvas_sub,self.finish_canvas)
        if tag == 101:
            self.text__finish.set('黒の勝ちです')
        elif tag == 85:
            self.text__finish.set('白の勝ちです')

    def move_log(self,x,y):
        ex = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}
        self.update_log(str(self.hold_piece[2]) + "," + ex[self.hold_piece[1]]
                        +"から"+ str(y) + "," + ex[x] + '\n')
        if 77<=self.hold_piece[0] and self.hold_piece[0]<=84 \
            or 93<=self.hold_piece[0] and self.hold_piece[0]<=100:
            self.update_log("ポーンが")
        elif self.hold_piece[0] == 89 or self.hold_piece[0] == 90 \
            or self.hold_piece[0] == 105 or self.hold_piece[0] == 106:
            self.update_log("ルークが")
        elif self.hold_piece[0] == 86 or self.hold_piece[0] == 87 \
            or self.hold_piece[0] == 102 or self.hold_piece[0] == 103:
            self.update_log("ナイトが")
        elif self.hold_piece[0] == 75 or self.hold_piece[0] == 76 \
            or self.hold_piece[0] == 91 or self.hold_piece[0] == 92:
            self.update_log("ビショップが")
        elif self.hold_piece[0] == 88 or self.hold_piece[0] == 104:
            self.update_log("クイーンが")
        elif self.hold_piece[0] == 85 or self.hold_piece[0] == 101:
            self.update_log("キングが")

    def on_pieces(self):
        self.donlord()
        for piece in self.pieces:
            for x in piece['point']['x']:
                self.canvas_sub.create_image(x,piece['point']['y'],
                image=piece['img'])

    def chess_stage(self):
        self.canvas_sub.create_rectangle(0,0,500,500,fill="#a87900")
        for y in range(8):
            self.canvas_sub.create_text(25, y*50+75,text=y+1,fill="#000000",font=30)
            if y % 2 == 0:
                for x in range(8):
                    if x % 2 == 0:
                        self.canvas_sub.create_rectangle(x*50+50,y*50+50,x*50+100,y*50+100,fill="#DAA520")
                    else:
                        self.canvas_sub.create_rectangle(x*50+50,y*50+50,x*50+100,y*50+100,fill="#FFF8DC")
            elif y % 2 != 0:
                for x in range(8):
                    if x % 2 == 0:
                        self.canvas_sub.create_rectangle(x*50+50,y*50+50,x*50+100,y*50+100,fill="#FFF8DC")
                    else:
                        self.canvas_sub.create_rectangle(x*50+50,y*50+50,x*50+100,y*50+100,fill="#DAA520")
        self.canvas_sub.create_text(250, y*50+125,text='A        B       C        D        E        F        G        H',fill="#000000",font=30)
    
    def delete_pieces(self):
        self.delete_message = tk.Label(self.canvas_sub,
                            width = 10,
                            font =("",20),
                            text='取られた駒')
        self.delete_message.place(x=600,y=250)

    def turn_change(self):
        if self.turn == True:
            self.turn = False
            self.text__turn.set('今のターンは黒')
            if self.automatic_swich == True:
                self.stage.after(1000,self.automatic_start)
        elif self.turn == False:
            self.turn = True
            self.text__turn.set('今のターンは白')
    
    def turn_log(self):
        self.text__turn = tk.StringVar()
        self.text__turn.set('今のターンは白')
        text_turn = tk.Label(self.canvas_sub,
                            width = 20,
                            font =("",20),
                            textvariable = self.text__turn)
        text_turn.place(x=540,y=0)

    def finish_log(self):
        self.text__finish = tk.StringVar()
        self.text__finish.set('の勝ち？')
        text_finish = tk.Label(self.finish_canvas,
                            width = 20,
                            font =("",20),
                            textvariable = self.text__finish)
        text_finish.place(x=310,y=200)

    def click_check(self,tag):
        if self.turn == True:
            if 91<=tag and tag<=106 or 107<=tag:
                return(True)
        elif self.turn == False:
            if 75<=tag and tag<=90 or 107<=tag:
                return(True)

    def click(self,e):
        x = e.x#_root - self.canvas_sub.winfo_rootx()
        y = e.y#_root - self.canvas_sub.winfo_rooty()
        tag = self.canvas_sub.find_closest(x, y)[0]
        if self.click_check(tag):
            self.piece_move(tag,x,y)

    def mouse_move(self,e):
        x = e.x#_root - self.canvas_sub.winfo_rootx()
        y = e.y#_root - self.canvas_sub.winfo_rooty()
        ex = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}
        if x>=50 and y>=50 and x<=449 and y<=449:
            self.mouse_point["text"] = str(y//50) + ", " + ex[x//50]
        else:
            self.mouse_point["text"] = '座標無し'

    def mouse(self):
        self.mouse_point = tk.Label(self.canvas_sub,
                            width = 10,
                            font =("",20))
        self.mouse_point.place(x=600,y=75)

    def change_frame(self,old,new):
        old.place_forget()
        new.place(x=0,y=0)
        if new == self.canvas_sub:
            self.sounds('start')

    def start_button(self):
        button = ButtonPro("","","",self.canvas_main,text = 'チェスをする')
        button["command"] = lambda : self.change_frame(self.canvas_main,self.canvas_sub)
        button.place(x=410,y=222)

    def creat_log(self):
        self.log_label = ScrolledText(self.canvas_sub, font=("", 15), height=4, width=38)
        self.log_label.place(x=501,y=150)
        self.update_log('----ログ----\n')

    def update_log(self,message):
        self.log_label.insert('1.0',message)

    def return_move(self):
        tag = self.move_memory[-1][2]
        x = -self.move_memory[-1][0]
        y = -self.move_memory[-1][1]
        self.canvas_sub.move(tag,x*50,y*50)
        if self.move_memory[-1][3] == True:
            de = self.delete_memory[-1]
            self.canvas_sub.moveto(de[2],de[0]*50+3,de[1]*50+3)
            del self.delete_memory[-1]
        del self.move_memory[-1]

    def return_check(self):
        if len(self.move_memory) == 0:
            pass
        else:
            self.return_move()
            if self.automatic_swich == True:
                self.return_move()
            self.sounds('return')
            if self.automatic_swich == False:
                self.turn_change()

    def return_button(self):
        button = ButtonPro("","","",self.canvas_sub,text = '戻る')
        button["command"] = lambda : self.return_check()
        button.place(x=469,y=450)
    
    def reset_move(self):
        for i in self.marks:
            self.canvas_sub.delete(i)
        self.marks = []
        while len(self.move_memory) != 0:
            self.return_check()
        self.update_log('リセットしました\n')

    def reset_button(self):
        button = ButtonPro("","","",self.canvas_sub,text = 'リセット')
        button["command"] = lambda : self.reset_move()
        button.place(x=456,y=475)

    def automatic_on(self):
        self.automatic_swich = True

    def automatic_start(self):
        while True:
            tag = random.randint(75,90)
            x = self.canvas_sub.bbox(tag)[0]
            y = self.canvas_sub.bbox(tag)[1]
            self.piece_move(tag,x,y)
            if len(self.marks) != 0:
                break
        tag = self.marks[random.randint(0,len(self.marks)-1)]
        x = self.canvas_sub.bbox(tag)[0]
        y = self.canvas_sub.bbox(tag)[1]
        self.piece_move(tag,x,y)

    def sound_donlord(self):
        mixer.init()
        self.sound_attack = mixer.Sound("効果音.mp3/attack.mp3")
        self.sound_move = mixer.Sound("効果音.mp3/move.mp3")
        self.sound_return = mixer.Sound("効果音.mp3/return.mp3")
        self.sound_start = mixer.Sound("効果音.mp3/start.mp3")

    def sounds(self,kind):
        if self.sound_swich == True:
            if kind == 'attack':
                self.sound_attack.play()
            elif kind == 'move':
                self.sound_move.play()
            elif kind == 'return':
                self.sound_return.play()
            elif kind == 'start':
                self.sound_start.play()

    def sound_volume(self):
        self.sound_message = tk.Label(self.canvas_sub,
                            width = 10,
                            font =("",15),
                            text='音量')
        self.sound_message.place(x=430,y=505)
        self.scale_var = tk.DoubleVar()
        self.scaleH = tk.Scale( self.canvas_sub, 
                    variable = self.scale_var, 
                    command = self.sound_scroll,
                    orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                    length = 300,           # 全体の長さ
                    width = 20,             # 全体の太さ
                    sliderlength = 20,      # スライダー（つまみ）の幅
                    from_ = 0,            # 最小値（開始の値）
                    to = 10,               # 最大値（終了の値）
                    resolution=1,         # 変化の分解能(初期値:1)
                    tickinterval=1         # 目盛りの分解能(初期値0で表示なし)
                    )
        self.scaleH.place(x=505,y=485)

    def sound_scroll(self,event=None):
        self.sound_attack.set_volume((float)(self.scaleH.get()/10))
        self.sound_move.set_volume((float)(self.scaleH.get()/10))
        self.sound_return.set_volume((float)(self.scaleH.get()/10))
        self.sound_start.set_volume((float)(self.scaleH.get()/10))
        self.sound_move.play()
    
    def restart(self):
        self.reset_move()
        self.change_frame(self.finish_canvas,self.canvas_sub)

    def restart_button(self):
        button = ButtonPro("","","",self.finish_canvas,text = 'もう一回スタートする')
        button["command"] = lambda : self.restart()
        button.place(x=400,y=275)

    def all_finish(self):
        if len(self.move_memory) != 0:
            self.yml.append_date(self.move_memory,self.delete_memory)
        self.stage.destroy()

    def all_finish_button(self):
        button = ButtonPro("","","",self.finish_canvas,text = '終わる')
        button["command"] = lambda : self.all_finish()
        button.place(x=430,y=330)
        button = ButtonPro("","","",self.canvas_sub,text = '終わる')
        button["command"] = lambda : self.all_finish()
        button.place(x=859,y=525)

    def load(self):
        self.change_frame(self.canvas_main,self.canvas_sub)
        self.move_memory = self.yml.load_move_memory()
        delete_date = self.yml.load_delete_memory()
        self.delete_memory
        for move_date in self.move_memory:
            tag = move_date[2]
            x = move_date[0]
            y = move_date[1]
            self.canvas_sub.move(tag,x*50,y*50)
            if move_date[3] == True:
                self.delete_memory.append(delete_date[0])
                tag = delete_date[0][2]
                self.delete_move(tag)
                del  delete_date[0]
            self.turn_change()

    def load_button(self):
        button = ButtonPro("","","",self.canvas_main,text = 'チェスの続きをする')
        button["command"] = lambda : self.load()
        button.place(x=393,y=252)

    def creat_button(self):
        self.start_button()
        self.load_button()
        self.return_button()
        self.reset_button()
        self.restart_button()
        self.all_finish_button()

    def creat_stage(self):
        self.chess_stage()
        self.on_pieces()
    
    def creat_support(self):
        self.mouse()
        self.delete_pieces()
        self.creat_log()
        self.turn_log()
        self.finish_log()
        self.sound_volume()

    def program(self):
        self.creat_button()
        self.creat_stage()
        self.creat_support()
        self.canvas_sub.bind("<ButtonPress-1>", self.click)
        self.canvas_sub.bind("<Motion>", self.mouse_move)
        self.stage.protocol("WM_DELETE_WINDOW",self.all_finish)
        self.stage.mainloop()


if __name__ == '__main__':
    def start():
        stage = tk.Tk()
        stage.geometry("900x551")
        stage.title('チェス')
        app = Chess(stage)
        app.program()

start()