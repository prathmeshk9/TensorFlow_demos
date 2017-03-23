import csv
import numpy as np
from sklearn.svm import SVR
import matplot.pyplot as plt

dates = []
prices = []

def get_data(filename):
	with open(filename,'r') as csvfile:
	   csavFileReader = csv.reader(csvfile)
	   next(csvFileReader)
	   for row in csvFileReader:
	       dates.append(int(row[0].split('-')[0]))
		   prices.append(float(row[1]))
	return
	
def predict_price(dates,prices,x):
    dates = np.reshape(dates,len(dates),1)
	
	svr_len = SVR(kernel='linear',c=1e3)
	svr_poly = SVR(kernel='poly',c=1e3,degree=2)
	svr_len = SVR(kernel='rbf',c=1e3,gamma=0.1)
	svr_lin.fit(dates,prices)
	svr_poly.fit(dates,prices)
	svr_rbf.fit(dates,prices)
	
	plt.scatter(dates,prices,color='black', label='Data')
	plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
	plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
	plt.plot(dates, svr_ply.predict(dates), color='blue', label='Ploynomial model')
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('Support Vector Regration')
	plt.legend()
	plt.show()
	
	return svr_rbf.predict(x)[0],svr_lin.predict(x)[0], ,svr_poly.predict(x)[0]
	
get_data('aapl.csv')

predicted)price = predict_price(dates,price,29)

print(predicted_price)

plt.switch_backend('new_backend')
