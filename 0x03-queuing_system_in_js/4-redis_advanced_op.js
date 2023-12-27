import { createClient, print } from "redis";

const client = createClient();

client.on('error', err => {
  console.log(`Redis client not connected to server: ${err}`)
});

client.on('connect', () => {
  console.log(`Redis client connected to server`)
});

client.hset(
  "HolbertonSchools",
  "Portland",
  50,
  print
);

client.hset(
  "HolbertonSchools",
  "Seattle",
  80,
  print
);

client.hset(
  "HolbertonSchools",
  "New York",
  20,
  print
);

client.hset(
  "HolbertonSchools",
  "Bogota",
  20,
  print
);

client.hset(
  "HolbertonSchools",
  "Cali",
  40,
  print
);

client.hset(
  "HolbertonSchools",
  "Paris",
  2,
  (err, reply) => {
    if (err) {
      console.error('Error:', err);
    } else {
      console.log('Reply:', reply);
      // Retrieve the hash using hgetall
      client.hgetall('HolbertonSchools', (err, obj) => {
        if (err) {
          console.error('Error:', err);
        } else {
          console.log(obj);
          // Close the Redis connection
          client.quit();
        }
      });
    }
  }
);
