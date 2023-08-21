const dotenv = require('dotenv')
const amqp = require('amqplib/callback_api');

dotenv.config()

const RMQ_HOST = process.env.RMQ_HOST;
const RMQ_USER = process.env.RMQ_USER;
const RMQ_PASS = process.env.RMQ_PASS;
const RMQ_EXCHANGE = process.env.RMQ_EXCHANGE;


amqp.connect(`amqp://${RMQ_USER}:${RMQ_PASS}@${RMQ_HOST}`, function(error0, connection) {
    if (error0) {
        throw error0;
    }
    connection.createChannel(function(error1, channel) {
        if (error1) {
            throw error1;
        }

        var msg = 'DA DA DATA!';

        channel.assertExchange(RMQ_EXCHANGE, "direct", {
            durable: true
        });
        
        channel.publish(RMQ_EXCHANGE, "", Buffer.from(msg));

        console.log(" [x] Sent %s", msg);
    });
    setTimeout(function() {
        connection.close();
        process.exit(0);
    }, 500);
});