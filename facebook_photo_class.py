import quandl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea

dataset=quandl.get("WIKI/FB", authtoken='8DmUha6Zsgj_ZsDzYyK4')
dataset=dataset.drop(['Open','High','Low','Close','Volume','Ex-Dividend','Split Ratio'],axis=1)

dataset['HL_PCT']=(dataset['Adj. High']-dataset['Adj. Low'])/dataset['Adj. Close']
dataset['PCT_Change']=(dataset['Adj. Close']-dataset['Adj. Open'])/dataset['Adj. Open']
dataset=dataset[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

dataset['Label']=dataset['Adj. Close'].shift(-1)
dataset2=dataset.drop(['Label'],1)

dataset3=pd.DataFrame()
dataset3['Adj_Close']=dataset['Adj. Close']
dataset3['HL_PCT']=dataset['HL_PCT']
dataset3['PCT_Change']=dataset['PCT_Change']
dataset3['Adj_Volume']=dataset['Adj. Volume']
dataset3['Label']=dataset['Label']
dataset3=dataset3.dropna()

dataset4=pd.DataFrame()
dataset4['Adj_Close']=dataset['Adj. Close']
dataset4['HL_PCT']=dataset['HL_PCT']
dataset4['PCT_Change']=dataset['PCT_Change']
dataset4['Adj_Volume']=dataset['Adj. Volume']

class adjclose_label():
    
    def histplot(self):
         sea.set(style='darkgrid')
         plt.hist(dataset3.Adj_Close)
         plt.xlabel('Adj_Close')

    def implot(self):
        sea.lmplot(x='Adj_Close',y='Label',data=dataset3,fit_reg=False)
        plt.title('Adj_Close vs Label')
        
    def displot(self):
        sea.distplot(dataset3.Adj_Close,kde=False)
        
    def datasetplot(self):
        dataset3[['Adj_Close']].plot(legend=True,figsize=(10,4),subplots=True)
    

class hlpct_label():
    
    def histplot(self):
        plt.hist(dataset3.HL_PCT)
        plt.xlabel('HL_PCT')
        
    def implot(self):
        sea.lmplot(x='HL_PCT',y='Label',data=dataset3,fit_reg=False)
        plt.title('HL_PCT vs Label')

    def displot(self):
        sea.distplot(dataset3.HL_PCT,kde=False)
        
    def datasetplot(self):
        dataset3[['HL_PCT']].plot(legend=True,figsize=(10,4),subplots=True)

class pctchange_label():
    
    def histplot(self):
       plt.hist(dataset3.PCT_Change)
       plt.xlabel('PCT_change')
       
    def implot(self):
        sea.lmplot(x='PCT_Change',y='Label',data=dataset3,fit_reg=False)
        plt.title('PCT_Change vs Label')

    def displot(self):
        sea.distplot(dataset3.HL_PCT,kde=False)
    
    def datasetplot(self):
        dataset3[['PCT_Change']].plot(legend=True,figsize=(10,4),subplot=True)
        
class volume_label():
    
    def histplot(self):
        plt.hist(dataset3.Adj_Volume)
        plt.xlabel('Adj_Volume')

    def implot(self):
        sea.lmplot(x='Adj_Volume',y='Label',data=dataset3,fit_reg=False)
        plt.title('Adj_Volume vs Label')

    def displot(self):
        sea.distplot(dataset3.Adj_Volume,kde=False)
        
    def datasetplot(self):
        dataset3[['Adj_Volume']].plot(legend=True,figsize=(10,4),subplot=True)
        
