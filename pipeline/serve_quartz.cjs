// Reuse Quartz's installed server: its links require extensionless HTML URLs.
const http = require("node:http")
const path = require("node:path")
const serve = require("../quartz/node_modules/serve-handler")
const port = Number(process.argv[2] || 8080)
http.createServer((req, res) => {
  serve(req, res, { public: path.resolve(__dirname, "../quartz/public"), cleanUrls: true })
    .catch(() => { res.statusCode = 500; res.end("Unable to serve page") })
}).listen(port, "127.0.0.1", () => console.log(`Wiki: http://127.0.0.1:${port}`))
