from google.cloud import storage
from google.oauth2 import service_account
import rasterio

# Set the credentials
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

import numpy as np
sen2decband2 = np.nan_to_num(sen2decband)
sen2janband2 = np.nan_to_num(sen2janband)


n = 0
csvlistsen2dec = []
csvlistsen2jan = []

x, y, z = (sen2decband2.shape)

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

