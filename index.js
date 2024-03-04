const express = require("express");
const app = express();

app.use(express.static("build/html"));
const path = require("path");
app.get("*", (req, res) => {
    console.log(path.resolve(__dirname, "build", "html", "index.html"));
    res.sendFile(path.resolve(__dirname, "build", "html", "index.html"));
});

const port = process.env.PORT || 5000;
app.listen(port);