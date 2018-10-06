from tkinter.ttk import Notebook
from tkinter import ttk
import facebook_gui_visual_class_import as graph
import facebook_gui_predict_class_import as predict
class Autoresized_Notebook(Notebook):
    def __init__(self, master=None, **kw):
        
        Notebook.__init__(self, master, **kw)
        self.bind("<<NotebookTabChanged>>", self._on_tab_changed)

    def _on_tab_changed(self,event):
        
        event.widget.update_idletasks()
        tab = event.widget.nametowidget(event.widget.select())
        event.widget.configure(height=tab.winfo_reqheight(),width=tab.winfo_reqwidth())

if __name__== "__main__":
    from tkinter import Frame, Tk
    root = Tk()      
    style = ttk.Style()

    style.theme_create( "project", parent="alt", settings={
        "TNotebook.Tab": {"configure": {"padding": [50,10],"font":'Arial'},
            "map":       {"background": [("selected", '#f2f2f2')] } } } )
    style.theme_use("project")
    root.resizable(0,0)
    notebook = Autoresized_Notebook(root)    
    Tab1=Frame(notebook, width=1000, height=1000)
    predict=predict.predict_price(Tab1)
    predict.price()
    Tab2=Frame(notebook, width=1700, height=800)
    visual=graph.visual(Tab2)
    visual.phot()
    notebook.add(Tab1,text="Price")
    notebook.add(Tab2,text="Visulization")
    notebook.grid(ipadx=50)
    root.mainloop()
    
    



