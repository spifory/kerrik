import Command from '../handlers/commands.js';

export const command: Command = {
    name: 'upsince',
    description: 'See how long I\'ve been online',
    aliases: ['uptime', 'up-since'],
    callback: (bot, msg, args) => {
        // create a stringUpTime constant that will return in the following format: YYYY-MM-DD HH:MM:SS E.g. 2023-02-01 23:59:39
        const stringUpTime = new Date(bot.startTime).toLocaleString('en-ZA')
        // create a upTime constant that will return in the following format: HH:MM:SS E.g. 23:59:39
        const upTime = Math.round(bot.startTime / 1000)
        // send a message to the channel that the command was sent in
        bot.sendMessage(`I've been online since ${stringUpTime} <t:${upTime}:R>`)
    }
}