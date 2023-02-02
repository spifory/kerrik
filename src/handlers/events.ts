import path from 'path';

import { Message } from 'evangeline';
import { fileURLToPath } from 'url';
import { readdirSync } from 'fs';

import { Kerrik } from '../bot.js';

export default interface Event<EventName extends keyof ClientEvents> {
    name: EventName;
    callback: (bot: Kerrik, ...args: ClientEvents[EventName]) => void;
}

interface ClientEvents {
    ready: [];
    messageCreate: [Message];
    close: [number, Buffer];
    error: [Error]
}

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export const loadEvents = (bot: Kerrik) => {
    readdirSync(path.join(__dirname, '..', 'events')).forEach(async (file) => {
        const event = (await import(path.join(__dirname, '..', 'events', file))).default;
        try {
            bot.on(event.name, event.callback.bind(null, bot));
            console.info(`\`${file}\` event listener`);
        } catch (e) {
            console.trace(`[E] Error loading ${file}: ${e}`);
            console.warn('[W] Exiting...');
            process.exit(1);
        }
    });
};
