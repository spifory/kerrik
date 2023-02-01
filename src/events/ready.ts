import Event from '../handlers/events';

export const event: Event<'ready'> = {
    name: 'ready',
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    callback: (_bot) => {
        console.info('[I] Kerrik is ready!');
    }
};