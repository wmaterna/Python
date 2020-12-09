from cmath import cos, sin
import random
from tkinter import *
import tkinter as tk
import graph_class


if __name__ == '__main__':



    g = graph_class.Graph()
    root = Tk()
    root.title("Wizualizacja grafu")
    root.geometry("800x800")
    root.configure(bg='#EDF6F9')
    myLabel = Label(root, text="Wprowadz dane: ", fg='#006D77',bg='#EDF6F9',font='Helvetica 18 bold')
    myLabel.grid(row=1, column=1)
    Label(root, text=" ", bg='#EDF6F9').grid(row=0, column=1)
    var = BooleanVar() #var for checkbox


    def create_circle(x, y, r, canvasName):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, fill='#83C5BE', outline='#006D77')


#an correction to edges_drawing, without it all edges stars and ends in the middle of
#vertex, causing illegibility of vertex label
    def rightPosition(x, y):
        if (x < 250 and x > 50) and (y < 391 and y > 108):
            return 20, 0
        if (x >= 108 and x <= 391) and (y <= 450 and y >= 250):
            return 0, -20
        if (x >= 250 and x <= 450) and (y <= 391 and y >= 108):
            return -20, 0
        if (x >= 108 and x <= 391) and (y >= 50 and y <= 250):
            return 0, 20
        else:
            return 0, 0


#drawing lines or arrows beetween vertexes
    def edges_drawing(dictX, dictY):
        for u in g:
            x = dictX[u.get_id]
            y = dictY[u.get_id]
            connectedV = u.get_connections()
            for q in connectedV:
                weight = u.get_weight(q)
                xcon = dictX[q.get_id]
                ycon = dictY[q.get_id]
                middleX = (x + xcon) / 2
                middleY = (y + ycon) / 2
                text_box = myCanvas.create_text(middleX + 10, middleY + 10, fill='#006D77', text=weight)
                correctionXforBeg, correctionYforBeg = rightPosition(x, y)
                print(correctionXforBeg, correctionYforBeg)
                correctionXforEnd, correctionYforEnd = rightPosition(xcon, ycon)
                print(correctionXforEnd, correctionYforEnd)

                if var.get() == 0:
                    myCanvas.create_line(x + correctionXforBeg, y + correctionYforBeg, xcon + correctionXforEnd,
                                              ycon + correctionYforEnd, arrow='last', fill='#006D77')
                else:
                    myCanvas.create_line(x + correctionXforBeg, y + correctionYforBeg, xcon + correctionXforEnd,
                                              ycon + correctionYforEnd, fill='#006D77')


#counting  x,y points on circle due to number of elements in graph
#returning an array of coordinates

    def points():
        numofvertex = g.vert_count
        alpha = (2 * 3.14) / numofvertex
        coordinatesX = []
        coordinatesY = []
        for v in range(numofvertex):
            cosinus = cos(alpha * v)
            sinus = sin(alpha * v)
            xn = 250 + (200 * cosinus)
            print(xn.real)
            coordinatesX.append(xn.real)
            yn = 250 + (200 * sinus)
            print(yn.real)
            coordinatesY.append(yn.real)
        return coordinatesX, coordinatesY

#button function to add connection beetween vertexes
    def add_edge_clicked():
        vert_1 = f_vertex.get()
        vert_2 = s_vertex.get()
        value_edge = e_value.get()

        if var.get() == 0:
            g.add_edge(vert_1, vert_2, value_edge)

        else:
            g.add_both_edges(vert_1, vert_2, value_edge)
        f_vertex.delete(0, END)
        s_vertex.delete(0, END)
        e_value.delete(0, END)


#Printing vertexes on screen, printing control output on cmd
    def vertex_printing():
        i = 0
        dictX = {}
        dictY = {}
        tabVertexTemp = []
        for v in g:
            coordinatesX, coordinatesY = points()

            create_circle(coordinatesX[i], coordinatesY[i], 20, myCanvas)
            label = v.get_id()
            dictX[v.get_id] = coordinatesX[i]
            dictY[v.get_id] = coordinatesY[i]
            myCanvas.create_text(coordinatesX[i], coordinatesY[i], fill='#006D77', text=label,
                                      font='Helvetica 14 bold')
            i = i + 1

        edges_drawing(dictX, dictY)

        for v in g:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                print((vid, wid, v.get_weight(w)))

        for from_id in g.get_vertices():
            t = tuple(v.id for v in g.get_vertex(from_id).adjacent.keys())
            print(f"edge: {from_id} to : {t}")



#Checkbutton
    c = Checkbutton(root, text="Graf nieskierowany", variable=var, fg='#006D77',bg='#EDF6F9')
    c.deselect()
    c.grid(row=8,column=1)


#Entry
    f_vertex = Entry(root, width=30)
    f_vertex.grid(row=2, column=1, padx=20)

    s_vertex = Entry(root, width=30)
    s_vertex.grid(row=3, column=1, padx=20)

    e_value = Entry(root, width=30)
    e_value.grid(row=4, column=1, padx=20)

#EntryLabels
    Label(root, text=" ", bg='#EDF6F9').grid(row=5, column=1)
    f_vertex_label = Label(root, text="Pierwszy wierzchołek",fg='#006D77',bg='#EDF6F9',font='Helvetica 18')
    f_vertex_label.grid(row=2, column=0)

    s_vertex_label = Label(root, text="Drugi wierzchołek",fg='#006D77',bg='#EDF6F9',font='Helvetica 18')
    s_vertex_label.grid(row=3, column=0)

    t_vertex_label = Label(root, text="Waga krawędzi ",fg='#006D77',bg='#EDF6F9',font='Helvetica 18')
    t_vertex_label.grid(row=4, column=0)

#Buttons
    button_add = Button(root, text="Dodaj krawedz", padx=20, command=add_edge_clicked, fg='#006D77', bg='#EDF6F9', activeforeground='#83C5BE', font='Helvetica')
    button_add.grid(row=7,column=1)

    button_view = Button(root, text="Pokaz graf", padx=20, command=vertex_printing, fg='#006D77', bg='#EDF6F9', activeforeground='#83C5BE', font='Helvetica')
    button_view.grid(row=9,column=1)

    Label(root, text=" ", bg='#EDF6F9').grid(row=10, column=1)

#Canvas
    myCanvas = Canvas(root, height=500, width=500, bg='#EDF6F9')
    myCanvas.grid(row=11,column=1)
    Label(root, text=" ", bg='#EDF6F9').grid(row=12, column=1)



    root.mainloop()
