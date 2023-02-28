import { Component, OnInit } from '@angular/core';
import { Farm } from '../models/Farm';
import { Owner } from '../models/Owner';

@Component({
	selector: 'app-new-farm',
	templateUrl: './new-farm.component.html',
	styleUrls: ['./new-farm.component.scss']
})
export class NewFarmComponent implements OnInit {

	constructor() { }

	public mockOnwer: Owner = {
		name: "Leo",
		document: "123",
		document_type: 'CPF',
		creation_date: new Date()
	}

	public fazenda: Farm = {
		name: "string",
		geomtry: "any",
		area: 1,
		centroid: [0],
		creation_date: new Date(),
		owner: this.mockOnwer
	}

	ngOnInit(): void {
	}

	public onSubmit() {
		console.log(this.fazenda)
	}

}