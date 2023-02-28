import { createClient, print } from 'redis';
import {  promisify } from 'util';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print)
}

const displaySchoolValue = async (schoolName) => {
    const res = await promisify(client.GET).bind(client)(schoolName);
    console.log(res);
}

const main = async () => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco')
}

client.on('connect', async () => {
    console.log('Redis client connected to the server');
    await main()
  });
