import xarray as xr
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


ds = xr.open_dataset('era5_uk_temp_2024.nc')

# Convert to Celsius and get numpy array
t2m = ds['t2m'].values - 273.15  # shape (366, 41, 49)

# Flatten each day's grid into a 1D vector
X = t2m[:-1].reshape(365, -1)  # features: days 1-365, shape (365, 2009)
y = t2m[1:].mean(axis=(1, 2))  # targets: mean temp days 2-366, shape (365,)

print("X shape:", X.shape)
print("y shape:", y.shape)
print("Example target values:", y[:5].round(1))

# Normalise features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42) #20% of set is put into test set and 80% for training set. Data is shuffled randomly using seed 42

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate on test set
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.2f}°C")
print(f"R²: {r2:.3f}")

# Sort test set by date for time series plot
sort_idx = np.argsort(y_test)

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(range(len(y_test)), y_test[sort_idx], label='Actual', color='blue')
ax.plot(range(len(y_test)), y_pred[sort_idx], label='Predicted', color='red', linestyle='--')
ax.set_xlabel('Sample (sorted by temperature)')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Actual vs Predicted — sorted by temperature')
ax.legend()
plt.savefig('ml_predictions.png', dpi=150, bbox_inches='tight')