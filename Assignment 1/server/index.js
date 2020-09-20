const express = require("express")
// const responseTime = require("response-time")
const app = express()
const port = 8080

function fibo(n) { 
        
            if (n < 2)
                return 1;
            else   return fibo(n - 2) + fibo(n - 1);
}
app.use(express.json());
app.get("/", (req, res) => {
    res.send("Hello World")
})
app.get("/fibo", (req, res) => {
    res.send({"number":fibo(Math.floor(Math.random()*10+30))})
})
app.post("/", (req, res) => {
    console.debug(req.body.text)
    res.send(JSON.stringify({ "output": req.body.text.split("").reverse().join("") }))
})

app.listen(port, () => console.log("Example app listening on port ${port}!"))
