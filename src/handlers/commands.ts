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
}

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export const loadCommands = (bot: Kerrik) => {
    readdirSync(path.join(__dirname, '..', 'commands')).forEach(async (file) => {
        const { command } = await import(path.join(__dirname, '..', 'commands', file));
        bot.executeCommand(command.name, command.aliases || [], command.callback);
    });
};