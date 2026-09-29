#Q06
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("house_prices.csv")
X = df[["size_sqft", "rooms", "age_years", "distance_km"]]
y = df["price_lkr_mn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

intercept = model.intercept_
c1, c2, c3, c4 = model.coef_

print(round(intercept,4), round(c1,4), round(c2,4), round(c3,4), round(c4,4))  # 6a

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(round(mae,4), round(rmse,4), round(r2,4))  # 6b

new_house = pd.DataFrame([[1800, 3, 12, 8]], columns=["size_sqft", "rooms", "age_years", "distance_km"])
pred_price = model.predict(new_house)[0]

print(round(pred_price,4))  # 6c