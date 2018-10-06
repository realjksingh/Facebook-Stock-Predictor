
class visual():
    def __init__(self,tab):
        self.tab=tab
    def phot(self):
        import tkinter as tk
        import facebook_photo_class as graph
        close_label=graph.adjclose_label()
        hlpct_label=graph.hlpct_label() 
        pctchg_label=graph.pctchange_label()
        volume_label=graph.volume_label()
        
        
        label11=tk.Label(self.tab,text='Visualization',justify=tk.CENTER,font=('Arial Bold Italic',40))
        label11.grid(column=0,row=0,columnspan=9)
        
        label12=tk.Label(self.tab,text='Carat vs Price',font=('Arial Bold Italic',20))
        label12.grid(column=0,row=1,ipadx=30)
        
        button=tk.Button(self.tab,text='Histogram',height=3,width=10,command=close_label.histplot)
        button.grid(column=0,row=2,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Scatterplot Colorless',height=3,width=10,command=close_label.implot)            
        button.grid(column=0,row=3,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Scatterplot Color',height=3,width=10,command=close_label.displot)
        button.grid(column=0,row=4,pady=20,ipadx=30)
        
        button=tk.Button(self.tab,text='Scatterplot Cut',height=3,width=10,command=close_label.datasetplot)
        button.grid(column=0,row=5,pady=20,ipadx=30)

        
        label13=tk.Label(self.tab,text='Cut vs Price',font=('Arial Bold Italic',20))
        label13.grid(column=1,row=1,ipadx=30)

        button=tk.Button(self.tab,text='Countplot',height=3,width=10,command=hlpct_label.histplot)
        button.grid(column=1,row=2,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Boxplot',height=3,width=10,command=hlpct_label.implot)
        button.grid(column=1,row=3,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Violinplot',height=3,width=10,command=hlpct_label.displot)
        button.grid(column=1,row=4,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Violinplot',height=3,width=10,command=hlpct_label.datasetplot)
        button.grid(column=1,row=5,pady=20,ipadx=30)
        
        label14=tk.Label(self.tab,text='Color vs Price',font=('Arial Bold Italic',20))
        label14.grid(column=2,row=1,ipadx=30)

        button=tk.Button(self.tab,text='Countplot',height=3,width=10,command=pctchg_label.histplot)
        button.grid(column=2,row=2,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Boxplot',height=3,width=10,command=pctchg_label.implot)
        button.grid(column=2,row=3,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Violinplot',height=3,width=10,command=pctchg_label.displot)
        button.grid(column=2,row=4,pady=20,ipadx=30)
        
        button=tk.Button(self.tab,text='Violinplot',height=3,width=10,command=pctchg_label.datasetplot)
        button.grid(column=2,row=5,pady=20,ipadx=30)

        label15=tk.Label(self.tab,text='Clarity vs Price',font=('Arial Bold Italic',20))
        label15.grid(column=3,row=1,ipadx=30)

        button=tk.Button(self.tab,text='Countplot',height=3,width=10,command=volume_label.histplot)
        button.grid(column=3,row=2,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Boxplot',height=3,width=10,command=volume_label.implot)
        button.grid(column=3,row=3,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Violinplot',height=3,width=10,command=volume_label.displot)
        button.grid(column=3,row=4,pady=20,ipadx=30)
        
        button=tk.Button(self.tab,text='Violinplot',height=3,width=10,command=pctchg_label.datasetplot)
        button.grid(column=3,row=5,pady=20,ipadx=30)

        