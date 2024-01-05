var ee = require('@google/earthengine');
var privateKey = require('/Users/saraswathyamjith/loggingdetector/loggingdetector-4094a78b71f7.json');

// Authenticate using a service account.
ee.data.authenticateViaPrivateKey(privateKey, function() {
  ee.initialize(null, null, function() {
    // ... run analysis ...
    var image = new ee.Image('srtm90_v4');
    image.getMap({min: 0, max: 1000}, function(map) {
             console.log(map);
      
    });
  }, function(e) {
    console.error('Initialization error: ' + e);
  });
}, function(e) {
  console.error('Authentication error: ' + e);
});
