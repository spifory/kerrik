import Event from '../handlers/events';

export default {
    name: 'ready',
    callback: (bot) => {
        console.info(`[I] ${bot.author} is ready!`);
    }
} as Event<'ready'>;
