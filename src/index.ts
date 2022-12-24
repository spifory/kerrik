import { Kerrik } from './bot.js'

const bot = new Kerrik()

bot.on('messageCreate', async (msg) => {
    const prefixes = ['-', 'kerrik ', 'kerrik']
    const prefix = prefixes.find((p) => msg.content.startsWith(p))
    if (!prefix) return

    const args = msg.content.slice(prefix.length).trim().split(/ +/)
    const command = args.shift()?.toLowerCase()

    if (command === 'ping') {
        bot.sendMessage('pong!')
    }
})

bot.connect()
