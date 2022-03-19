def main():
    root = Tk()
    root.wm_title("Crud Python MySQL")
    app = Ventana(root) #Recibe de la clase frame
    app.mainloop()

#Creamos punto de inicio

if __name__=="__main__":
    main()