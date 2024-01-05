
function maskS2clouds(image) {
    var qa = image.select('QA60');
  
    // Bits 10 and 11 are clouds and cirrus, respectively.
    var cloudBitMask = 1 << 10;
    var cirrusBitMask = 1 << 11;
  
    // Both flags should be set to zero, indicating clear conditions.
    var mask = qa.bitwiseAnd(cloudBitMask).eq(0)
        .and(qa.bitwiseAnd(cirrusBitMask).eq(0));
  
    return image.updateMask(mask);
  }
  
  
  //var batch = require('users/fitoprincipe/geetools:batch');
  var s2 = ee.ImageCollection("COPERNICUS/S2");
  var s1 = ee.ImageCollection("COPERNICUS/S1_GRD");
  //var admin2 = ee.FeatureCollection("FAO/GAUL_SIMPLIFIED_500m/2015/level3");
  
  var admin2 = ee.FeatureCollection("FAO/GAUL_SIMPLIFIED_500m/2015/level2");
  
  // var ariquemes = admin2.filter(ee.Filter.eq('ADM2_NAME', 'Ariquemes'));
  //var geometry =  ee.Geometry.Polygon([[-61.0, -6.0], [-60.5,-6.0],[-60.5, -5.5],  [-61.0, -5.5]]);
  //var geometry =  ee.Geometry.Polygon([[-65.999875, -9.000125], [-65.999875, -9.500125],
  //[-65.499875, -9.500125], [-65.499875, -9.000125]])
  
  
  // Extract specific percentiles
  var percentiles = s2.filterDate('2022-01-01', '2022-02-25')
    .filter(ee.Filter.bounds(geometry))
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 100))
    .map(maskS2clouds)
    .median()
    .select(['B2', 'B3', 'B4','B5', 'B6', 'B7', 'B8', 'B8A', 'B11', 'B12']);
    
  Map.addLayer(geometry)
  Map.centerObject(geometry)
  
  var rgbVis = {
    min: 0,
    max: 4000,
    bands: ['B4', 'B3', 'B2'],
  };
  Map.addLayer(percentiles, rgbVis, 'RGB');
  
  // Plot a few bands on the map
  Export.image.toDrive({
      image: percentiles.clip(geometry),
      description: 'sen2amazon',
      folder: 'sen2amazon',
      fileNamePrefix: 'sen2amazontest-jan',
      region: geometry,
      scale: 10,
      maxPixels: 1e12
  })
  