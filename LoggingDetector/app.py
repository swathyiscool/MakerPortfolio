from flask import Flask, jsonify, render_template
from google.cloud import storage
import os
from google.cloud import storage
from google.oauth2 import service_account
import rasterio
import csv
import numpy as np
import xgboost as xgb
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

import matplotlib.pyplot as plt
from google.cloud import storage
from google.oauth2 import service_account
import rasterio


app = Flask(__name__)

# Set the path to the service account key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/saraswathyamjith/loggingdetector/loggingdetector-4094a78b71f7.json'

@app.route("/")
def home():
    return render_template("page.html")


@app.route('/model')
def model():
    try: 
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



        return jsonify({
            "success": True,
            "message": "The file was successfully checked."
        })

    except Exception as e:
        print(e)
        return jsonify({
            "success": False,
            "message": "There was an error checking the file."
        })
    # Set the credentials

@app.route('/check-file')
def check_file():
    try: 
        credentials = service_account.Credentials.from_service_account_file('/Users/saraswathyamjith/loggingdetector/loggingdetector-4094a78b71f7.json')

        # Create the client object
        client = storage.Client(project='loggingdetector', credentials=credentials)

        bucket = client.get_bucket('loggindetector')


        # Gets the file you want to download
        blob = bucket.blob('sen2amazontest-dec3.tif')

        # Downloads the file to your local machine
        blob.download_to_filename('/Users/saraswathyamjith/loggingdetector/sen2amazontest-dec3.tif')

        # Gets the file you want to download
        blob2 = bucket.blob('sen2amazontest-jan3.tif')

        # Downloads the file to your local machine
        blob2.download_to_filename('/Users/saraswathyamjith/loggingdetector/sen2amazontest-jan3.tif')

        ### extracting the lat/long coordinates for pixels with deforestation
        sentinel2dec = rasterio.open('/Users/saraswathyamjith/loggingdetector/sen2amazontest-dec3.tif')
        sentinel2jan = rasterio.open('/Users/saraswathyamjith/loggingdetector/sen2amazontest-jan3.tif')

        sen2decband = sentinel2dec.read()
        print(sen2decband.shape)

        sen2janband = sentinel2jan.read()
        print(sen2janband.shape)

        sen2decband2 = np.nan_to_num(sen2decband)
        sen2janband2 = np.nan_to_num(sen2janband)


        n = 0
        csvlistsen2dec = []
        csvlistsen2jan = []

        x, y, z = (sen2decband2.shape)

        sen2dec3x3 = np.zeros((10, 3, 3))
        sen2jan3x3 = np.zeros((10, 3, 3))

        for sen2drow in range (0, y-3,3):
        
            for sen2dcol in range (0, z-3,3):

                if (sen2drow>=3 and sen2dcol>=3 ):
                    sen2dec3x3 = sen2decband[:, sen2drow-1:sen2drow+2, sen2dcol -1:sen2dcol +2]
                    sen2jan3x3 = sen2janband[:, sen2drow-1:sen2drow+2, sen2dcol -1:sen2dcol +2]


                rowvalssen2dec = []
                rowvalssen2jan = []
                

            for e in range (0, x):
                
                avgvalsen2j = 0
                avgvalsen2d = 0
                for c in range(3):
                    for d in range(3):
                        if sen2dec3x3.shape[1] > 0 and sen2dec3x3.shape[2] > 0:
                            avgvalsen2d += sen2dec3x3[e, c, d]
                            avgvalsen2j += sen2jan3x3[e, c, d]
                rowvalssen2dec.append(avgvalsen2d / 9)
                rowvalssen2jan.append(avgvalsen2d / 9)

            csvlistsen2dec.append(rowvalssen2dec)
            csvlistsen2jan.append(rowvalssen2jan)

        ## csv file
        import csv

        with open('output.csv', 'w', newline='') as file:
            writer = csv.writer(file)


        csvnddecsen2 = np.asarray(csvlistsen2dec)
        csvndjansen2 = np.asarray(csvlistsen2jan)
        print(csvnddecsen2.shape)
        print(csvndjansen2.shape)


        combinedsen2 = np.concatenate([csvnddecsen2, csvndjansen2], axis=1)
        print(combinedsen2.shape)

        import csv

        s2_bands = ['B2', 'B3', 'B4','B5', 'B6', 'B7', 'B8', 'B8A', 'B11', 'B12']

        s1_bands = ['VV', 'VH']

        s1_bands_all = ['classifcation'] + [b + "dec" for b in s1_bands] + [b + "jan" for b in s1_bands]

        s2_bands_all =  [b + "dec" for b in s2_bands] + [b + "jan" for b in s2_bands]

        combinedfields = s1_bands_all + s2_bands_all[1:]
        fieldssen1 = ['classification', 'VVdec', 'VHdec', 'VVjan', 'VHjan']
        filenamesen2 = "/Users/saraswathyamjith/loggingdetector/sen2test.csv"


        f = open(filenamesen2, "w")
        f.truncate()
        f.close()



        with open(filenamesen2, 'w', newline='') as csvfilesen2:
            csvwriter2 = csv.writer(csvfilesen2)
            csvwriter2.writerow(s2_bands_all)
            csvwriter2.writerows(combinedsen2)



        # create blob object and upload file to cloud storage
        blob = bucket.blob('sen2testcsv')
        blob.upload_from_filename('/Users/saraswathyamjith/loggingdetector/sen2test.csv')


        
        return jsonify({
            "success": True,
            "message": "The file was successfully checked."
        })

    except Exception as e:
        print(e)
        return jsonify({
            "success": False,
            "message": "There was an error checking the file."
        })
    # Set the credentials


if __name__ == '__main__':
    app.run(debug=True)
