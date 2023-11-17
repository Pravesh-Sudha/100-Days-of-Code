const http = require('http');

const port = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type','text/html')
    res.end('<h1>This is Leefo WebPage</h1> <p>This Page Belong to leefo</p>')
})

server.listen(port, () => {
    
    console.log(`Server is Listening on Port.. ${port}`)

});