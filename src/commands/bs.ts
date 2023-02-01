import Command from '../handlers/commands.js';

export default {
    name: 'bs',
    description: 'Determine how much a you or a person is spewing',
    aliases: ['bs-o-metre', 'bs-metre'],
    callback: (bot, msg, args) => {
        const random_bs_level = Math.floor(Math.random() * 100);
        let user = args.slice(0).join(' ');

        if (user) {
            user = `**${user}**`;
        } else {
            user = `**${msg.author.trim()}**`;  // trim because peoples' usernames have whitespaces to fuck with Enoki :)
        }

        const responses = {
            0: `${user}'s a fucking saint.`,
            50: `Something tells me that ${user} is full of bullshit but are bullshitting about it.`,
            75: `${user} lives off of bullshit, ${user} is full of shit, everything ${user} utters is bullshit.`
        };

        // eslint-disable-next-line @typescript-eslint/no-unused-vars
        for (const [_, __] of Object.entries(responses)) {
            if (random_bs_level >= 75) {
                return bot.sendMessage(`**${random_bs_level}%** ${responses[75]}`);
            } else if (random_bs_level >= 50 && random_bs_level < 75) {
                return bot.sendMessage(`**${random_bs_level}%** ${responses[50]}`);
            } else if (random_bs_level >= 0 && random_bs_level < 50) {
                return bot.sendMessage(`**${random_bs_level}%** ${responses[0]}`);
            }
        }
    }
} as Command;
