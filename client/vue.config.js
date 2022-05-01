const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
    // publicPath: process.env.NODE_ENV === 'production'
    // ? 'repo-name'
    // : '.',
    outputDir: 'production',
    assetsDir: '',
    indexPath: 'index.html',
    pages: {
        index: {
            entry: 'src/app.js'
        }
    }
})