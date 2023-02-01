import { Bot, Message } from 'evangeline';


export class Kerrik extends Bot {
    startTime!: number
    constructor() {
        super("Kerrik")
        
        this.on('ready', () => {
            this.startTime = Date.now()
            console.info(`[I] startTime set to ${this.startTime} (${new Date(this.startTime).toLocaleString()})`)
        })
    }

    async addCommand(
        name: string,
        aliases: string[],
        callback: (bot: Kerrik, msg: Message, args: string[]) => void) {
            this.on('messageCreate', async (msg) => {
                const prefixes = ["kerrik", "kerrik ", "-"]
                const prefix = prefixes.find(p => msg.content.startsWith(p))
                if (!prefix) return;

                const args = msg.content.slice(prefix.length).trim().split(/ +/g);
                const command = args.shift()?.toLowerCase();
                if (command === name || aliases && aliases.includes(command!)) {
                    callback(this, msg, args)
                }
            })
        }
}
