import { creatClient, createClient } from 'redis';

function redisConnect() {
  const client = createClient();
  client.on('connect', () => {
    console.log('Redis client connected to the server')
  }).on('err', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
  });
};
redisConnect();
