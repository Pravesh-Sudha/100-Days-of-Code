const express = require('express')
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
    res.send("This is my node application of CICD Demo")
})

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}/`);
});
