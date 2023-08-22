import dotenv from 'dotenv';

dotenv.config()

export const context = {
    PROTO_PATH: process.env.PROTO_PATH,
    GRPC_HOST: process.env.GRPC_HOST,
    REMOTE_PORT: process.env.REMOTE_PORT,
    RMQ_HOST: process.env.RMQ_HOST,
	RMQ_PORT:process.env.RMQ_PORT,
	RMQ_USER:process.env.RMQ_USER,
	RMQ_PASS:process.env.RMQ_PASS,
	RMQ_QUEUE:process.env.RMQ_QUEUE,
	RMQ_EXCHANGE:process.env.RMQ_EXCHANGE,
    RMQ_TYPE:process.env.RMQ_TYPE
};