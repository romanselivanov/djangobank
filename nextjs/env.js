const apiHost = process.env.NEXT_PUBLIC_API_HOST;
const apiPort = process.env.NEXT_PUBLIC_API_PORT;
const apiProto = process.env.NEXT_PUBLIC_API_PROTO;

const apiUrl = `${apiProto}://${apiHost}:${apiPort}`;

module.exports = {
    apiUrl,
}