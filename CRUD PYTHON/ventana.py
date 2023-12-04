from tkinter import *
from tkinter import ttk
import re

class Ventana(Frame):
    
    def __init__(self, master=None):
        super().__init__(master, width=1250, height=450)
        self.master = master
        self.pack()
        self.Usuario()
       
    def fNuevo(self):
        pass

    def fAgregar(self):
        pass
   
    def fCancelar(self):
        pass

    def Usuario(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=0, width=93, height=680)

        self.btnNuevo = Button(frame1, text="Nuevo", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5, y=90, width=80, height=30)

        self.form_selector = ttk.Combobox(frame1, values=["Usuario"])
        self.form_selector.set("Usuario")
        self.form_selector.place(x=5, y=130, width=80, height=30)

        frame2 = Frame(self, bg="#d3dde3")
        frame2.place(x=95, y=0, width=160, height=680)

        lbl1 = Label(frame2, text="Nombre")
        lbl1.place(x=3, y=5)

        self.txtNombre = Entry(frame2)
        self.txtNombre.place(x=3, y=25, width=90, height=20)

        lbl2 = Label(frame2, text="Email")
        lbl2.place(x=3, y=50)

        self.txtEmail = Entry(frame2)
        self.txtEmail.place(x=3, y=70, width=130, height=20)

        lbl3 = Label(frame2, text="Telefono")
        lbl3.place(x=3, y=95)

        self.txtTelefono = Entry(frame2)
        self.txtTelefono.place(x=3, y=119, width=130, height=20)

        lbl4 = Label(frame2, text="Sexo")
        lbl4.place(x=3, y=140)

        self.txtSexo = Entry(frame2)
        self.txtSexo.place(x=3, y=160, width=20, height=20)

        lbl5 = Label(frame2, text="Fecha de nacimiento")
        lbl5.place(x=3, y=185)

        self.txtFecha = Entry(frame2)
        self.txtFecha.place(x=3, y=205, width=130, height=20)

        lbl6 = Label(frame2, text="Contraseña")
        lbl6.place(x=3, y=230)

        self.txtContraseña = Entry(frame2)
        self.txtContraseña.place(x=3, y=250, width=130, height=20)

        lbl7 = Label(frame2, text="Subtotal")
        lbl7.place(x=3, y=275)

        self.txtSubtotal = Entry(frame2)
        self.txtSubtotal.place(x=3, y=300, width=130, height=20)

        lbl8 = Label(frame2, text="Cantidad de producto")
        lbl8.place(x=3, y=325)

        self.txtCantidad = Entry(frame2)
        self.txtCantidad.place(x=3, y=349, width=130, height=20)

        self.btnAgregar=Button(frame2,text="Agregar",command=self.fAgregar,bg="green", fg="white")
        self.btnAgregar.place(x=3,y=380,width=75,height=30)
        self.btnCancelar = Button(frame2, text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80, y=380, width=75, height=30)

        self.grid=ttk.Treeview(self, columns=("col1","col2","col3","col4","col5","col6","col7","col8"))

        self.grid.column("#0",width=40,anchor=CENTER,stretch=False)
        self.grid.column("col1",width=100,anchor=CENTER,stretch=False)
        self.grid.column("col2",width=100,anchor=CENTER,stretch=False)
        self.grid.column("col3",width=100,anchor=CENTER,stretch=False)
        self.grid.column("col4",width=40,anchor=CENTER,stretch=False)
        self.grid.column("col5",width=100,anchor=CENTER,stretch=False)
        self.grid.column("col6",width=100,anchor=CENTER,stretch=False)
        self.grid.column("col7",width=100,anchor=CENTER,stretch=False)
        self.grid.column("col8",width=100,anchor=CENTER,stretch=False)

        self.grid.heading("#0",text="Id",anchor=CENTER)
        self.grid.heading("col1",text="Nombre",anchor=CENTER)
        self.grid.heading("col2",text="Email",anchor=CENTER)
        self.grid.heading("col3",text="Telefono",anchor=CENTER)
        self.grid.heading("col4",text="Sexo",anchor=CENTER)
        self.grid.heading("col5",text="Fecha Nacimiento",anchor=CENTER)
        self.grid.heading("col6",text="Contraseña",anchor=CENTER)
        self.grid.heading("col7",text="SubTotal",anchor=CENTER)
        self.grid.heading("col8",text="Cantidad Productos",anchor=CENTER)

        self.grid.place(x=256,y=0,width=1500,height=259)
        self.grid.insert("", END, text="1", values=("Pancho", "pancho@email.com", "123456789", "M", "01/01/2000", "********", "$100.00", "5"))


# Crea la ventana principal
root = Tk()
app = Ventana(master=root)
app.mainloop()