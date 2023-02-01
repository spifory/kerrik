import Command from '../handlers/commands.js';

export default {
    name: 'upsince',
    description: 'See how long I\'ve been online',
    aliases: ['uptime', 'up-since'],
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    callback: (bot, _msg, _args) => {
        const stringUpTime = new Date(bot.startTime).toLocaleString('en-ZA');
        bot.sendMessage(`I've been online since ${stringUpTime}`);
    }
} as Command;
