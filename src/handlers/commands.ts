import path from 'path';

import { Message } from 'evangeline';
import { fileURLToPath } from 'url';
import { readdirSync } from 'fs';

import { Kerrik } from '../bot.js';

export default interface Command {
    name: string;
    description: string;
    aliases?: string[];
    callback: (bot: Kerrik, msg: Message, args: string[]) => void;
};

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export const loadCommands = (bot: Kerrik) => {
    readdirSync(path.join(__dirname, '..', 'commands')).forEach(async (file) => {
        if (file.startsWith('_')) {
            return;
        }
        const command: Command = (await import(path.join(__dirname, '..', 'commands', file))).default;
        try {
            bot.executeCommand(command.name, command.aliases || [], command.callback);
            console.info(`\`${command.name}\` command loaded`);
        } catch (e) {
            console.trace(`[E] Error loading \`${file}\`: ${e}`);
            console.warn('[E] Exiting...');
            process.exit(1);
        }
    });
};
