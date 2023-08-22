import amqp from 'amqplib/callback_api.js';
import { context } from './context.js';

export const Run = async (request, response) => {
    amqp.connect(`amqp://${context.RMQ_USER}:${context.RMQ_PASS}@${context.RMQ_HOST}`, (err, conn) => {
        if (err) {
            throw err;
        }

        publish(conn, request, response);
    });
} 

const publish = (conn, request, response) => {
    conn.createChannel((err, channel) => {
        if (err) {
            throw err;
        }

        const msg = 'DA DA DATA!';

        channel.assertExchange(context.RMQ_EXCHANGE, context.RMQ_TYPE, {
            durable: true
        });

        const isPublished = channel.publish(context.RMQ_EXCHANGE, "", Buffer.from(msg));

        if (isPublished) {
            response.send(" [x] Sent: " + msg);
            setTimeout( () => conn.close(), 100);
        }
    });
}