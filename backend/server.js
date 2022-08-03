// create express app on port 3000
const { exec } = require('child_process');
const express = require('express');
const app = express();
// import cors from 'cors';
const cors = require("cors")
const whitelist = ["http://localhost:3001"]
const corsOptions = {
    origin: function (origin, callback) {
        if (!origin || whitelist.indexOf(origin) !== -1) {
            callback(null, true)
        } else {
            callback(new Error("Not allowed by CORS"))
        }
    },
    credentials: true,
}
app.use(cors(corsOptions))
app.use(express.json());
const port = 3000;
app.listen(port, () => console.log(`Example app listening on port ${port}!`));
app.get('/', async (req, res) => {
    res.send('Hello World!');
});

const SYSTEM_COMMANDS = [{ command: "ifconfig", }, { command: "uptime", }, { command: "date", }]
// for each system command, create a route
SYSTEM_COMMANDS.forEach(command => {
    app.get(`/${command.command}`, (req, res) => {
        exec(`${command.command} | jc --${command.command} --pretty`, (error, stdout, stderr) => {
            if (error) {
                console.error(`error: ${error.message}`);
                return;
            }

            if (stderr) {
                console.error(`stderr: ${stderr}`);
                return;
            }
            let json = JSON.parse(stdout);
            console.log(`stdout:\n${stdout}`);
            res.status(200).json(json);
        })
    });
});

app.get('/list_storage_devices', (req, res) => {
    exec(`ls /dev/disk/by-id/ | jc --ls --pretty`, (error, stdout, stderr) => {
        if (error) {
            console.error(`error: ${error.message}`);
            return;
        }

        if (stderr) {
            console.error(`stderr: ${stderr}`);
            return;
        }
        let json = JSON.parse(stdout);
        console.log(`stdout:\n${stdout}`);
        res.status(200).json(json);
    })
});
