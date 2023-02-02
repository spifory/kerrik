import Event from '../handlers/events.js';

export default {
    name: 'messageCreate',
    async callback(bot, msg) {
        if (msg.content.startsWith('!speed')) {
            return await bot.sendMessage('Wrong, I am faster\'er');
        }
    }
} as Event<'messageCreate'>;