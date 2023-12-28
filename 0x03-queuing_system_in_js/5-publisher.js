import { createClient, print } from "redis";

const client = createClient();

client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
  console.log(`Redis client connected to the server`);
});

function publishMessage(message, time) {
  setTimeout(() => {
    client.publish("holberton school channel", message);
  },
  time );
};

publishMessage("Holberton Studnt #1 starts course", 100);
publishMessage("Holberton Studnt #2 starts course", 200);
publishMessage("KILL SERVER", 300);
publishMessage("Holberton Studnt #3 starts course", 400);
