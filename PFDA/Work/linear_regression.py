import numpy as np
from sklearn.linear_model import LinearRegression

model = LinearRegression()


model.fit(x, y)


r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
#coefficient of determination: 0.715875613747954



# predicted response 
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')