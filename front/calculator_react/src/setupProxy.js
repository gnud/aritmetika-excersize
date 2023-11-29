const { createProxyMiddleware } = require('http-proxy-middleware');

const API_URL = process.env.API_URL;
const API_REWRITE = process.env.API_REWRITE;

const proxy = {
    target: API_URL,
    changeOrigin: true,
    pathRewrite: {
        [API_REWRITE]: '/'
    }
}
module.exports = function(app) {
  app.use(
    API_REWRITE,
    createProxyMiddleware(proxy)
  );
};