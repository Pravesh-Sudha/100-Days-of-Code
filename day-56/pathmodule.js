const path = require('path');

console.log(path.extname(__filename));
//return .js

console.log(path.basename('/foo/bar/baz/asdf/quux.html'))
//returns quux.html