import xgboost as xgb
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

import matplotlib.pyplot as plt
from google.cloud import storage
from google.oauth2 import service_account
import rasterio

# Set the credentials
credentials = service_account.Credentials.from_service_account_file('/Users/saraswathyamjith/loggingdetector/loggingdetector-4094a78b71f7.json')

# Create the client object
client = storage.Client(project='loggingdetector', credentials=credentials)

bucket = client.get_bucket('loggindetector')


# Gets the file you want to download

# Gets the file you want to download
blob2 = bucket.blob('sent2x2.csv')

# Downloads the file to your local machine
blob2.download_to_filename('/Users/saraswathyamjith/loggingdetector/sent2x2.csv')

### extracting the lat/long coordinates for pixels with deforestation
sentinel2dec = rasterio.open('/Users/saraswathyamjith/loggingdetector/sen2amazontest-dec3.tif')

data2 = pd.read_csv("/Users/saraswathyamjith/loggingdetector/sen2test.csv")
data = pd.read_csv("/Users/saraswathyamjith/loggingdetector/sent2x2.csv")

data["NDVI_dec"] = (data["B8dec"] - data["B4dec"])  / (data["B8dec"] + data["B4dec"])
data["NDVI_jan"] = (data["B8jan"] - data["B4jan"])  / (data["B8jan"] + data["B4jan"])


data2["NDVI_dec"] = (data2["B8dec"] - data2["B4dec"])  / (data2["B8dec"] + data2["B4dec"])
data2["NDVI_jan"] = (data2["B8jan"] - data2["B4jan"])  / (data2["B8jan"] + data2["B4jan"])

print(data.head())

X_train = data.iloc[:, 1:]
y_train = data.iloc[:, 0]

X_test = data2

dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test)

params = {
    'max_depth': 7,
    'eta': 0.1,
    'objective': 'binary:logistic',
    'eval_metric': 'logloss',
    'seed': 42,
}

model = xgb.train(params, dtrain, num_boost_round=100)

y_pred = model.predict(dtest)
y_pred = np.round(y_pred)


import seaborn as sns


sen2decband = sentinel2dec.read()

dims, nrows, ncols = sen2decband.shape
y_pred = np.reshape(y_pred, (int(nrows/3) -1 , int(ncols /3) -2))

colors = ['#CAEABD', '#F8E35C' , '#F85C5C']
# Generate a heatmap of predictions for each pixel in the testing dataset
sns.heatmap(y_pred, cmap=colors)

# Save the heatmap to a PNG file
plt.savefig('/Users/saraswathyamjith/loggingdetector/heatmap.png')

accuracy = None
f1 = None
precision = None
recall = None
print("Predictions saved to 'heatmap.png'")


