import StreamrClient from "streamr-client";
import crypto from "crypto";
import { writeFile } from 'fs';
import { promisify } from 'util';

const streamId = "streams.dimo.eth/firehose/weather";
const writeToFile = promisify(writeFile);  // Convert callback-based function to promise-based

const main = async () => {
  // Create the client using the validated private key
  const client = new StreamrClient({
    auth: {
      privateKey: crypto.randomBytes(32).toString("hex"),
    },
  });

  const stream = await client.getStream(streamId);

  const onMessage = async (content) => {
    const extractedData = {
      id: content.id,
      ambientTemp: content.data.ambientTemp,
      latitude: content.data.latitude,
      longitude: content.data.longitude,
      time: content.time,
    };
    
    const dataString = JSON.stringify(extractedData, undefined, 2) + '\n';  // Format data as string with newline for each entry
    await writeToFile('output.txt', dataString, { flag: 'a' });  // Write to output.txt, appending each new entry
  };
  
  const subscriptions = await Promise.all(
    stream.getStreamParts().map(async (partition) => {
      await client.subscribe(
        partition,
        onMessage
      );
    })
  );
  return { client, subscriptions };
};

export default main();
