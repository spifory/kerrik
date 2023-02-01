import Event from '../handlers/events'

export const event: Event<'ready'> = {
    name: 'ready',
    callback: (_bot) => {
        console.info(`[I] Kerrik is ready!`)
    }
}