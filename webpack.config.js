const path = require('path');

module.exports = {
  target: 'node', // Set the target as Node.js
  entry: './src/main.js', // Entry file of your Node.js application
  output: {
    path: path.resolve(__dirname, 'dist'), // Output directory
    filename: 'bundle.js', // Output file name
    libraryTarget: 'commonjs2', // Specify the module type
  },
  mode: 'development',
  // Add other configurations as needed, e.g., loaders, plugins, etc.
};
