import { Bot } from 'evangeline';


export class Kerrik extends Bot {
	startTime!: number
	constructor() {
		super("Kerrik")
		
		this.on('ready', () => {
			this.startTime = Date.now()
			console.info(`${this.name} is ready`)
		})
	}
}
