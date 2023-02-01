import Event from '../handlers/events'

export const event: Event<'ready'> = {
    name: 'ready',
    callback: (bot) => {
        console.info(`[I] Kerrik is ready!`)
    }
}