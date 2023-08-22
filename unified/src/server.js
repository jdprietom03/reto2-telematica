import express from "express";
import { context } from "./context.js";
import { Run as RungRPC } from "./grpc-run.js";
import { Run as RunAMQP } from "./amqp-run.js";

const app = express();

app.get('/', (request, response) => {
	response.send("Pong!")
});

app.get('/amqp', (request, response) => {
	RunAMQP(request, response);
});

app.get('/grpc', (request, response) => {
	RungRPC(request, response);
});

app.listen(context.REMOTE_PORT, err => {
	if (err) {
		console.error("Error escuchando: ", err);
		return;
	}

	console.log(`Listen to port: ${context.REMOTE_PORT}`);
});