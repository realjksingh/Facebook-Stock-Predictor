class predict_price():
    def __init__(self,tab):
        self.tab=tab
    def price(self):
        import tkinter as tk
        import pickle
        import pandas as pd
        file=open('reg.txt','rb')
        reg=pickle.load(file)
        file2=open('reg_scaler.txt','rb')
        scaler=pickle.load(file2)
        reg_dic={'Linear Regression':reg[0],'Support Vector Machine':reg[1],'Lasso Regression':reg[2],
            'Ridge Regression':reg[3],'Ada Boosting':reg[4],'Gradient Boosting':reg[5],
            'Decision Tree':reg[6],'Random Forest':reg[7]}
        def correct(inp,type):
            try:
                if(type== '1' ):
                    if inp.find(' ') == -1:
                        inp=float(inp.strip())
                        return True
                    else:
                        return False
                elif(type== '0'):
                    return True
            except ValueError:
                return False
    
        def predict():
            if e1.get() !='' and e2.get() !='' and e3.get() !='' and e4.get() !='' and e5.get() !='':
                opening,closing,high=float(e1.get()),float(e2.get()),float(e3.get())
                low,volume=float(e4.get()),float(e5.get())
                HL_PCT=(high-low)/(closing)*100
                PCT_Change=(opening-closing)/closing*100
                X_debug={'closing':[closing],'HL_PCT':[HL_PCT],'PCT_Change':[PCT_Change],'volume':[volume]}
                X_debug=pd.DataFrame.tab(data=X_debug)
                X_debug=X_debug.iloc[:,:].values
                if(e6.get()=='Support Vector Machine'):
                    X_debug=scaler[0].transform(X_debug)
                    value=reg_dic[e6.get()].predict(X_debug)
                    value=scaler[1].inverse_transform(value)
                else:
                    value=reg_dic[e6.get()].predict(X_debug)
                label7.configure(text=value)
            else:
                label7.configure(text='Enter the Required Value\'s' )

        label=tk.Label(self.tab,text='Price',font=('Arial Bold Italic',40))
        label.grid(column=0,row=0,columnspan=2)

        reg=self.tab.register(correct)

        label1=tk.Label(self.tab,text='Opening',font=('Arial Bold',20))
        label1.grid(column=0,row=1,sticky='W',padx=10,pady=10)
        e1=tk.Entry(self.tab,font=('Arial Bold',20))
        e1.grid(row=1,column=1)
        e1.config(validate='key',validatecommand=(reg,'%P','%d'))
        
        label2=tk.Label(self.tab,text='Closing',font=('Arial Bold',20))
        label2.grid(column=0,row=5,sticky='W',padx=10,pady=10)
        e2=tk.Entry(self.tab,font=('Arial Bold',20))
        e2.grid(row=5,column=1)
        e2.config(validate='key',validatecommand=(reg,'%P','%d'))
        
        label3=tk.Label(self.tab,text='High',font=('Arial Bold',20))
        label3.grid(column=0,row=6,sticky='W',padx=10,pady=10)
        e3=tk.Entry(self.tab,font=('Arial Bold',20))
        e3.grid(row=6,column=1)
        e3.config(validate='key',validatecommand=(reg,'%P','%d'))
        
        label4=tk.Label(self.tab,text='Low',font=('Arial Bold',20))
        label4.grid(column=0,row=7,sticky='W',padx=10,pady=10)
        e4=tk.Entry(self.tab,font=('Arial Bold',20))
        e4.grid(row=7,column=1)
        e4.config(validate='key',validatecommand=(reg,'%P','%d'))
        
        label5=tk.Label(self.tab,text='Volume',font=('Arial Bold',20))
        label5.grid(column=0,row=8,sticky='W',padx=10,pady=10)
        e5=tk.Entry(self.tab,font=('Arial Bold',20))
        e5.grid(row=8,column=1)
        e5.config(validate='key',validatecommand=(reg,'%P','%d'))
        
        label6=tk.Label(self.tab,text='Prediction Algo',font=('Arial Bold',20))
        label6.grid(column=0,row=9,padx=10,pady=10)
        algo=['Linear Regression','Support Vector Machine','Lasso Regression','Ridge Regression','Ada Boosting',
              'Gradient Boosting','Decision Tree','Random Forest']
        e6=tk.StringVar()
        e6.set('Linear Regression')
        popupmenu=tk.OptionMenu(self.tab,e6,*algo)
        popupmenu.configure(activebackground='#cecece',cursor='hand2',font=('Arial Bold',10))
        popupmenu.grid(column=1,row=9,sticky='ew',ipadx=10,pady=10)
        
        button=tk.Button(self.tab,text='Calculate',justify=tk.CENTER,height=3,width=10,command=predict)
        button.grid(column=0,row=10,columnspan=2,padx=10,ipadx=30)
        
        label7=tk.Label(self.tab,font=('Arial Bold',20))
        label7.grid(column=0,row=11,sticky='W',padx=10,pady=10,columnspan=2)
        
        
    