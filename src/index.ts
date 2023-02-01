import { Kerrik } from './bot.js';
import { loadCommands } from './handlers/commands.js';
import { loadEvents } from './handlers/events.js';

const bot = new Kerrik();

function main() {
    loadCommands(bot);
    loadEvents(bot);
    bot.connect();
}

main();