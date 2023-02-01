import Event from '../handlers/events';

export default {
    name: 'ready',
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    callback: (_bot) => {
        console.info('[I] Kerrik is ready!');
    }
} as Event<'ready'>;
