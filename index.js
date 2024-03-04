const express = require("express");
const app = express();

app.use(express.static("build/html"));
const path = require("path");
app.get("*", (req, res) => {
    res.sendFile(path.resolve(__dirname, "build", "html", "index.html"));
});

const port = process.env.port || 5000;
app.listen(port);