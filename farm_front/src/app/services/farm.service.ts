import { Injectable } from '@angular/core'
import { Farm } from './../models/Farm'
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
	providedIn: 'root',
})
export class FarmService {
	private apiUrl = 'http://localhost:8000/api/farms/';

	constructor(
		private http: HttpClient
	) {}

	create(farm: Farm): Observable<Farm> {
		return this.http.post<Farm>(this.apiUrl, farm);
	}

	read(id: number): Observable<Farm> {
		return this.http.get<Farm>(`${this.apiUrl}${id}/`);
	}

	list(): Observable<Farm[]> {
		return this.http.get<Farm[]>(this.apiUrl);
	}
}
