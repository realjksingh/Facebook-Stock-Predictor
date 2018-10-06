import numpy as np
import quandl
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
from sklearn.cross_validation import cross_val_score

from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor 
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor 

r2_scores=[]
dataset=quandl.get("WIKI/FB", authtoken='8DmUha6Zsgj_ZsDzYyK4')
dataset=dataset.drop(['Open','High','Low','Close','Volume','Ex-Dividend','Split Ratio'],axis=1)

dataset.info()

dataset['HL_PCT']=(dataset['Adj. High']-dataset['Adj. Low'])/dataset['Adj. Close']*100
dataset['PCT_Change']=(dataset['Adj. Close']-dataset['Adj. Open'])/dataset['Adj. Open']*100
dataset['Label']=dataset['Adj. Close'].shift(-1)
dataset=dataset.drop(['Adj. Open','Adj. High','Adj. Low'],axis=1)
dataset=dataset[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume','Label']]
dataset=dataset.dropna(axis=0)
X=dataset.iloc[:,:4].values
y=dataset.iloc[:,4].values

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
#To Get the row and column to calculate the R^2 Adjusted
n=X_train.shape[0]
p=X_train.shape[1]

#Linear Regression Model
reg_linear=LinearRegression()
reg_linear.fit(X_train,y_train)
y_pred_linear=reg_linear.predict(X_test)
print('1.Linear Regression')
print('Training Score: ' ,reg_linear.score(X_train,y_train))
print('Testing Score: ',reg_linear.score(X_test, y_test))
print('Mean Square Error:',mean_squared_error(y_test, y_pred_linear))
print('Mean Absolute Error:',mean_absolute_error(y_test, y_pred_linear))
print('Root Mean Square Error:',mean_squared_error(y_test, y_pred_linear)**0.5)
r2_linear=r2_score(y_test, y_pred_linear)
r2_linear=1-(((1-r2_linear)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_linear)
r2_scores.append(r2_linear)

#Support Vector Regression
sc_X=StandardScaler()
sc_y=StandardScaler()
X_svr=X
y_svr=y
y_svr_2=y
X_svr=sc_X.fit_transform(X_svr)
y_svr=sc_y.fit_transform(y_svr.reshape(-1,1)).reshape(-1)

X_train_svr,X_test_svr,y_train_svr,y_test_svr=train_test_split(X_svr,y_svr,test_size=.3)

reg_svr=SVR(kernel='rbf')
reg_svr.fit(X_train_svr,y_train_svr)
y_pred_svr=reg_svr.predict(X_test_svr)
print('2.Support Vector Regression("Kernel=RBF")')
print('Training Score : ',reg_svr.score(X_train_svr,y_train_svr))
print('Testing Score: ',reg_svr.score(X_test_svr, y_test_svr))
print('Mean Square Error:',mean_squared_error(y_test_svr, y_pred_svr))
print('Mean Absolute Error:',mean_absolute_error(y_test_svr, y_pred_svr))
print('Root Mean Square Error:',mean_squared_error(y_test_svr, y_pred_svr)**0.5)
r2_svr=r2_score(y_test_svr, y_pred_svr)
r2_svr=1-(((1-r2_svr)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_svr)
r2_scores.append(r2_svr)

#Lasso Linear Regression
reg_lasso = Lasso(normalize=True)
reg_lasso.fit(X_train , y_train)
y_pred_lasso = reg_lasso.predict(X_test)
print('3.Lasso Regression')
print('Training Score : ',reg_lasso.score(X_train,y_train))
print('Testing Score : ',reg_lasso.score(X_test, y_test))
print('Mean Square Error:',mean_squared_error(y_test, y_pred_lasso))
print('Mean Absolute Error:',mean_absolute_error(y_test, y_pred_lasso))
print('Root Mean Square Error:',mean_squared_error(y_test, y_pred_lasso)**0.5)
r2_lasso=r2_score(y_test, y_pred_lasso)
r2_lasso=1-(((1-r2_lasso)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_lasso)
r2_scores.append(r2_lasso)

#Ridge Linear Regression
reg_ridge= Ridge(normalize=True)
reg_ridge.fit(X_train , y_train)
y_pred_ridge = reg_ridge.predict(X_test)
print('4.Ridge Regression')
print('Training Score : ',reg_ridge.score(X_train, y_train))
print('Testing Score : ',reg_ridge.score(X_test, y_test))
print('Mean Square Error:',mean_squared_error(y_test, y_pred_ridge))
print('Mean Absolute Error:',mean_absolute_error(y_test, y_pred_ridge))
print('Root Mean Square Error:',mean_squared_error(y_test, y_pred_ridge)**0.5)
r2_ridge=r2_score(y_test, y_pred_ridge)
r2_ridge=1-(((1-r2_ridge)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_ridge)
r2_scores.append(r2_ridge)

#AdaBoost Regression Model
reg_ada = AdaBoostRegressor(n_estimators=1000)
reg_ada.fit(X_train , y_train)
y_pred_ada = reg_ada.predict(X_test)
print('5.AdaBoost Regression')
print('Training Score : ',reg_ada.score(X_train, y_train))
print('Testing Score : ',reg_ada.score(X_test, y_test))
print('Mean Square Error:',mean_squared_error(y_test, y_pred_ada))
print('Mean Absolute Error:',mean_absolute_error(y_test, y_pred_ada))
print('Root Mean Square Error:',mean_squared_error(y_test, y_pred_ada)**0.5)
r2_ada=r2_score(y_test, y_pred_ada)
r2_ada=1-(((1-r2_ada)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_ada)
r2_scores.append(r2_ada)

#Gradient Regression Model
reg_gradient = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1,max_depth=1, random_state=0, loss='ls',verbose = 1)
reg_gradient.fit(X_train , y_train)
y_pred_gradient = reg_gradient.predict(X_test)
print('6.Gradient Boosting Regression')
print('Training Score : ',reg_gradient.score(X_train, y_train))
print('Testing Score : ',reg_gradient.score(X_test, y_test))
print('Mean Square Error:',mean_squared_error(y_test, y_pred_gradient))
print('Mean Absolute Error:',mean_absolute_error(y_test, y_pred_gradient))
print('Root Mean Square Error:',mean_squared_error(y_test, y_pred_gradient)**0.5)
r2_gradient=r2_score(y_test, y_pred_gradient)
r2_gradient=1-(((1-r2_gradient)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_gradient)
r2_scores.append(r2_gradient)

#Random Forest Regression Model
k_scores=[]
for i in range(1,21):
    reg_random = RandomForestRegressor(n_estimators=i)
    scores=cross_val_score(reg_random,X,y,cv=10,scoring='mean_squared_error')    
    k_scores.append(np.sqrt(-scores).mean())
    i=i+1
reg_random = RandomForestRegressor(n_estimators=10)
reg_random.fit(X_train , y_train)
y_pred_random = reg_random.predict(X_test)
print('7.Random Forest')
print('Training Score : ',reg_random.score(X_train, y_train))
print('Testing Score : ',reg_random.score(X_test, y_test))
print('Mean Square Error:',mean_squared_error(y_test, y_pred_random))
print('Mean Absolute Error:',mean_absolute_error(y_test, y_pred_random))
print('Root Mean Square Error:',mean_squared_error(y_test, y_pred_random)**0.5)
r2_random=r2_score(y_test, y_pred_random)
r2_random=1-(((1-r2_random)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_random)
r2_scores.append(r2_random)

#K-NN regression Model
for i in range(1,21):
    reg_random = KNeighborsRegressor(n_neighbors=i)
    scores=cross_val_score(reg_random,X,y,cv=10,scoring='mean_squared_error')    
    k_scores.append(np.sqrt(-scores).mean())
    i=i+1
reg_knn = KNeighborsRegressor(n_neighbors=20)
reg_knn.fit(X_train , y_train)
y_pred_knn = reg_knn.predict(X_test)
print('8.KNeighbours Regression')
print('Training Score: ',reg_knn.score(X_train, y_train))
print('Testing Score : ',reg_knn.score(X_test, y_test))
print('Mean Square Error:',mean_squared_error(y_test, y_pred_knn))
print('Mean Absolute Error:',mean_absolute_error(y_test, y_pred_knn))
print('Root Mean Square Error:',mean_squared_error(y_test, y_pred_knn)**0.5)
r2_knn=r2_score(y_test, y_pred_knn)
r2_knn=1-(((1-r2_knn)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_knn)
r2_scores.append(r2_knn)

#To store the trained models
reg=[reg_linear,reg_svr,reg_lasso,reg_ridge,reg_ada,reg_gradient,reg_random,reg_knn]
scaler=[sc_X,sc_y]
file=open('reg.txt','wb')
file2=open('reg_score.txt','wb')
file3=open('reg_scaler.txt','wb')
pickle.dump(reg,file)
pickle.dump(r2_scores,file2)
pickle.dump(scaler,file3)
file.close()    