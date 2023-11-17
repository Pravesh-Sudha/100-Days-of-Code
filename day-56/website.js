const http = require('http');

const port = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    res.setHeader('Content-Type','text/html')

    if (req.url == '/') {
        res.statusCode = 200;
        res.end('<h1>This is Leefo WebPage</h1> <p>This Page Belong to leefo</p>')
    } else if(req.url == '/about') {
        res.statusCode = 200;
        res.end('<h1>This is Leefo About WebPage</h1> <p>This Page Belong to leefo about section</p>')
    }else {
        res.statusCode = 404;
        res.end('<h1>Error 404 not found</h1>');
    }
    
})

server.listen(port, () => {
    
    console.log(`Server is Listening on Port.. ${port}`)

});