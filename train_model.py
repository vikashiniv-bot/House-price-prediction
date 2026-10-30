
 
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
 
#loading the dataset
data = pd.read_csv("houseprice/house_data(in).csv")
#separate input fetures
X = data[['Size', 'Bedrooms', 'Age']]
# Target Variable
y = data['Price']
 
#create a model
model = LinearRegression()
 
#Train model
model.fit(X, y)
 
# save trained model
joblib.dump(model,'house_model.pkl')
print("Model trained and saved successfully")
 