const fs = require('fs');

const filePath = '/Users/saraswathyamjith/loggingdetector/Untitled design-10.png';

// check if the file exists before trying to delete it
if (fs.existsSync(filePath)) {
  fs.unlinkSync(filePath);
  console.log(`File ${filePath} deleted successfully`);
} else {
  console.log(`File ${filePath} does not exist`);
}
