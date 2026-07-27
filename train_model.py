import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
df = pd.read_csv(url)

# rm: average number of rooms, lstat: % lower status of population, ptratio: pupil-teacher ratio
features = ["rm", "lstat", "ptratio"]
X = df[features]
y = df["medv"]  # Median value of homes in $1000s

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train XGBoost model
model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("house price model trained and saved successfully!")