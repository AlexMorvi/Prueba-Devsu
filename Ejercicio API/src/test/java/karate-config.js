/**
 * Karate Test Configuration
 * Provides centralized configuration for PetStore Swagger API tests
 * 
 * API Behavior Notes:
 * - Standard REST API behavior: GET returns 404 for non-existent resources
 * - Tests follow create-first pattern to ensure data availability
 * - Each test scenario creates its own test data for independence
 * 
 * @returns {Object} Configuration object with environment settings
 */
function karateConfig() {
  // Environment-specific configuration
  var environment = karate.env || 'demo';
  karate.log('Running tests against PetStore Demo API in environment:', environment);
  
  // Base configuration object
  var config = {
    // API endpoints
    baseUrl: 'https://petstore.swagger.io/v2',
    apiVersion: 'v2',
    apiType: 'standard', // Standard REST API behavior
    
    // Test data configuration
    testData: {
      defaultTimeout: 10000,
      retryCount: 1, // Standard retry for network issues
      petIdRange: {
        min: 100000,
        max: 999999
      },
      // Test execution settings
      consistencyDelay: 1000, // Delay for data consistency
      cleanupEnabled: false // Manual cleanup for demo API
    }
  };
  
  // Environment-specific overrides
  if (environment === 'local') {
    config.baseUrl = 'http://localhost:8080/v2';
  }
  
  // Global timeout configurations
  karate.configure('connectTimeout', config.testData.defaultTimeout);
  karate.configure('readTimeout', config.testData.defaultTimeout);
  karate.configure('retry', { count: config.testData.retryCount, interval: 1000 });
  
  // SSL configuration for external APIs
  karate.configure('ssl', true);
  
  return config;
}