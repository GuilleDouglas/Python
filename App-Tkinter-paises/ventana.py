from select import select
from tkinter import *
from tkinter import ttk
from Countries import *
from tkinter import messagebox



class Ventana(Frame): 
    paises = Countries() #Paises es un objeto de la clase countries

   
   
   
    def __init__(self, master=None): #Constructor
        super().__init__(master,width=680, height=260) #ancho de 680 y alto de 260
        self.master = master
        self.pack() #para que se muestre los elementos
        self.create_widgets()
        self.llenaRegistros()
        self.habilitarCajas("disable")
        self.habilitarBtnOpen("normal")
        self.habilitarBtnGuardar("disable")
        self.id=-1 #cuando inicia tiene este valor y cuando modifiquemos, vamos a tomar esta variable

    
    
    
    def habilitarCajas(self,estado):
        self.txtISO3.configure(state=estado)
        self.txtCapital.configure(state=estado)
        self.txtCurrency.configure(state=estado)
        self.txtName.configure(state=estado)
        #self.txtISO3.configure(state="disable") #Deshabilitar caja
        #self.txtISO3.configure(state="normal")  #Habilitar caja
        
  
  
   
   
    def habilitarBtnOpen(self,estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

  
  
    def habilitarBtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)
        

    
    def limpiarCajas(self):
        self.txtCapital.delete  (0,END)
        self.txtCurrency.delete (0,END)
        self.txtName.delete     (0,END)
        self.txtISO3.delete     (0,END)
        pass

   
    def limpiagrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)


    def llenaRegistros(self):
        
        datos=self.paises.consulta_paises()
        
        for row in datos:
            #print(row[2]) #Imprime solo el nombre de los paises 
            self.grid.insert("",END,text=row[0], values=(row[1],row[2],row [3],row [4]))
       
        if len(self.grid.get_children()) > 0: #Estamos seguros que hay un elemento por lo menos
            self.grid.selection_set (self.grid.get_children()[0]) #seleccionamos el primer elemento
   
   
    def fNuevo(self):
        self.habilitarCajas("normal")
        self.habilitarBtnOpen("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()
        self.txtISO3.focus() #Coloca el cursor en la primera caja despues del click
        pass

    
    
    
    def fGuardar(self):
        if self.id==-1: #Estamos insertando nuevo registro
            messagebox.showinfo("Insertar", "Elemento insertado correctamente")
            self.paises.inserta_pais(self.txtISO3.get(),self.txtName.get(),self.txtCapital.get(),self.txtCurrency.get())
            
        else:           #Estamos haciendo una modificacion
            messagebox.showinfo("Modificar", "Elemento modificado correctamente")
            self.paises.Modifica_pais(self.id,self.txtISO3.get(),self.txtName.get(),self.txtCapital.get(),self.txtCurrency.get())
            self.id = -1 #Dejamos el id en su estado inicial

        self.limpiagrid()
        self.llenaRegistros()
        self.limpiarCajas()
        self.habilitarBtnGuardar("disable")
        self.habilitarBtnOpen("normal")
        self.habilitarCajas("disable")
    
    def fModificar(self):
        
        selected = self.grid.focus()
        clave = self.grid.item(selected,'text')
        
        if clave == '': #Si no hay elemento seleccionado la clave que es el id esta vacia 
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento')

        else:
            self.id=clave
            self.habilitarCajas("normal")
            valores = self.grid.item(selected,'values') # si hay elemento seleccionado sacamos los valores
            self.txtISO3.delete(0,END)
            self.limpiarCajas()
            self.txtISO3.insert(0,valores[0])
            self.txtName.insert(0,valores[1])
            self.txtCapital.insert(0,valores[2])
            self.txtCurrency.insert(0,valores[3])
            self.txtISO3.focus()
            self.habilitarBtnGuardar("normal")
            self.habilitarBtnOpen("disable")
            

            
            
            
    def fEliminar(self):
        
        #print(selected) #Imprime solo el Id seleccionado
        #row = self.grid.item(selected) #Nos va a dar todo el renglon
        #print(row) #Imprime todo  {'text': 26, 'image': '', 'values': ['OOO', 'AAAA', 'AAA', 'AAA'], 'open': 0, 'tags': ''}
        selected = self.grid.focus()
        clave = self.grid.item(selected,'text')
        if clave == '': #Si no hay elemento seleccionado la clave que es el id esta vacia 
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento')

        else:
            valores = self.grid.item(selected,'values') # si hay elemento seleccionado sacamos los valores
            data = str(clave) + " , "+valores[0]+ " , "+valores[1]
            r=messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado ?\n" +data)
    
            if r ==messagebox.YES:
                n = self.paises.elimina_pais(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", "Elemento Eliminado correctamente")
                    self.limpiagrid()
                    self.llenaRegistros()
                else:
                    messagebox.showwarning("Eliminar", "No fue posible eliminar")
    
    
    
    
    def fCancelar(self):
        r=messagebox.askquestion("Cancelar", "Estas seguro que deseas cancelar ?\n")
        
        if r ==messagebox.YES:
                self.limpiarCajas()
                self.habilitarBtnGuardar("disable")
                self.habilitarBtnOpen("normal")
                self.habilitarCajas("disable")
                self.id = -1 #Dejamos el id en su estado inicial
   
   
    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff") #Objeto de la clase frame
        frame1.place(x=0, y=0, width=93, height=259) #se ubica en la posicion con un ancho y alto

        self.btnNuevo=Button(frame1,text="Nuevo", command=self.fNuevo, bg="blue",fg="White") #letras en blanco fondo azul
        self.btnNuevo.place(x=5, y=50, width=80, height=30)


        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="blue",fg="White") #letras en blanco fondo azul
        self.btnModificar.place(x=5, y=90, width=80, height=30)


        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="blue",fg="White") #letras en blanco fondo azul
        self.btnEliminar.place(x=5, y=130, width=80, height=30)

        frame2 = Frame(self, bg="#d3dde3") #Objeto de la clase frame
        frame2.place(x=95, y=0, width=150, height=259) #se ubica en la posicion con un ancho y alto
        lbl1=Label(frame2,text="ISO3: ")
        lbl1.place(x=3, y=5) #No se pone ancho ni alto para que se ajuste al texto
        self.txtISO3=Entry(frame2)
        self.txtISO3.place(x=3,y=25,width=50, height=20)

        lbl2=Label(frame2,text="Country Name: ")
        lbl2.place(x=3, y=55) #No se pone ancho ni alto para que se ajuste al texto
        self.txtName=Entry(frame2)
        self.txtName.place(x=3,y=75,width=100, height=20)

        lbl3=Label(frame2,text="Capital: ")
        lbl3.place(x=3, y=105) #No se pone ancho ni alto para que se ajuste al texto
        self.txtCapital=Entry(frame2)
        self.txtCapital.place(x=3,y=125,width=100, height=20)

        lbl4=Label(frame2,text="Currency: ")
        lbl4.place(x=3, y=155) #No se pone ancho ni alto para que se ajuste al texto
        self.txtCurrency=Entry(frame2)
        self.txtCurrency.place(x=3,y=175,width=50, height=20)

        self.btnGuardar=Button( frame2, text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10, y=210, width=60, height=30)
        self.btnCancelar=Button( frame2, text="Cancelar", command=self.fCancelar, bg="green", fg="white")
        self.btnCancelar.place(x=80, y=210, width=60, height=30)

        frame3 = Frame(self, bg="yellow") 
        frame3.place(x=247, y=0, width=420, height=259) 


        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4"))

        self.grid.column("#0", width=70)
        self.grid.column("col1", width=80, anchor=CENTER)
        self.grid.column("col2", width=80, anchor=CENTER)
        self.grid.column("col3", width=80, anchor=CENTER)
        self.grid.column("col4", width=80, anchor=CENTER)

        #   Metodo heading modifico el encabezado
        self.grid.heading("#0",   text="Id" ,           anchor=CENTER)
        self.grid.heading("col1", text="ISO3",          anchor=CENTER)
        self.grid.heading("col2", text="Country Name",  anchor=CENTER)
        self.grid.heading("col3", text="Capital",       anchor=CENTER)
        self.grid.heading("col4", text="Currency Code", anchor=CENTER)

        self.grid.pack(side=LEFT)
        sb= Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)

        self.grid['selectmode']='browse' #aunque presionemos shift seleccionamos un solo elemento en la tabla

       # self.grid.insert("",END,text="1", values=("ARG","Argentina", "Buenos Aires", "ARS"))
