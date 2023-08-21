import amqp  from 'amqplib/callback_api';
import dotenv from 'dotenv';

dotenv.config()

const RMQ_HOST = process.env.RMQ_HOST;
const RMQ_USER = process.env.RMQ_USER;
const RMQ_PASS = process.env.RMQ_PASS;
const RMQ_EXCHANGE = process.env.RMQ_EXCHANGE;
const RMQ_PORT = process.env.RMQ_PORT;

const connectionProperties = {
  username: RMQ_USER,
  password: RMQ_PASS,
  port: RMQ_PORT,
  hostname: RMQ_HOST,
  vhost: '/',
};

amqp.connect(connectionProperties, (err, conn) => {
  if (err) {
    console.error(`Failed to connect to RabbitMQ: ${err}`);
    return;
  }

  conn.createChannel((err, channel) => {
    if (err) {
      console.error(`Failed to create a channel: ${err}`);
      return;
    }

    const msg = 'Hello, world!';

    channel.assertExchange(RMQ_EXCHANGE, "direct", {
      durable:  true
    });

    channel.publish(RMQ_EXCHANGE, "", Buffer.from(msg));
    console.log(`[x] Sent: ${msg}`);
  });

  setTimeout(() => {
    conn.close();
    process.exit(0);
  }, 500);
});
