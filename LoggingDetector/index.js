var ee = require('@google/earthengine');
var privateKey = require('/Users/saraswathyamjith/loggingdetector/loggingdetector-4094a78b71f7.json');

var initialize = function() {
  ee.initialize(null, null, function() {
    // ... run analysis ...
  }, function(e) {
    console.error('Initialization error: ' + e);
  });
};


const {Storage} = require('@google-cloud/storage');
const storage = new Storage({
  keyFilename: '/Users/saraswathyamjith/loggingdetector/loggingdetector-4094a78b71f7.json'
});



// Authenticate using a service account.
ee.data.authenticateViaPrivateKey(privateKey, initialize, function(e) {
  console.error('Authentication error: ' + e);
});
var cors = require('cors');
const app = require('express')();
app.use(cors());
var bodyParser  = require('body-parser');
app.use(bodyParser.json());
const PORT= 8080;
app.listen(PORT, () => {
    console.log(`Example app listening on port ${PORT}`)
  });

  app.post('/hello',cors(), (req, res) => {
    // Define the region of interest
var geometry = ee.Geometry.Polygon([[req.body.coordinates[0][0].lat,req.body.coordinates[0][0].lng], [req.body.coordinates[0][1].lat, req.body.coordinates[0][1].lng],
[req.body.coordinates[0][2].lat, req.body.coordinates[0][2].lng], [req.body.coordinates[0][3].lat, req.body.coordinates[0][3].lng]]);

  

  // Load the Sentinel-2 image collection
var s2 = ee.ImageCollection("COPERNICUS/S2");

// Filter the image collection by date, location, and cloud cover
var percentiles = s2.filterDate('2022-01-01', '2022-02-25')
  .filterBounds(geometry)
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 30))
  .median()
  .select(['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B8A', 'B11', 'B12']);

var percentilesdec = s2.filterDate('2020-11-01', '2020-12-26')
  .filterBounds(geometry)
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
  .median()
  .select(['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B8A', 'B11', 'B12']);

// Export the image to Google Cloud Storage
// Replace the Export.image.toDrive() function with the following code to export to Cloud Storage
var exportTask = ee.batch.Export.image.toCloudStorage({
  image: percentiles.clip(geometry),
  description: 'sen2amazon',
  bucket: 'loggindetector', // Replace with your Cloud Storage bucket name
  fileNamePrefix: 'sen2amazontest-jan2',
  region: geometry,
  scale: 10,
  maxPixels: 1e12
});

var exportTask2 = ee.batch.Export.image.toCloudStorage({
  image: percentilesdec.clip(geometry),
  description: 'sen2amazon2',
  bucket: 'loggindetector', // Replace with your Cloud Storage bucket name
  fileNamePrefix: 'sen2amazontest-dec2',
  region: geometry,
  scale: 10,
  maxPixels: 1e12
});

// Start the export task
exportTask.start(function(error, req,res) {
  if (error) {
    console.error('Export failed: ', error);
  } else {
    console.log('Export succeeded: ');
    
  }
});

exportTask2.start(function(error, req,res) {
  if (error) {
    console.error('Export failed: ', error);
  } else {
    console.log('Export2 succeeded: ');
    
  }
});

    res.json({Coordinates: req.body.coordinates[0][1].lat})  // <==== req.body will be a parsed JSON object
  })
