import { Component } from '@angular/core';
import { FarmService } from '../services/farm.service';
import { Farm } from '../models/Farm';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  template: `
    <h2>Farms</h2>
    <ul>
      <li *ngFor="let farm of farms" (click)="goToDetails(farm)">{{ farm.name }}</li>
    </ul>
    <p routerLink="farm">Cadastrar</p>
  `,
})
export class DashboardComponent {
  farms: Farm[] = [];

  constructor(
    private farmService: FarmService,
    private router: Router
  ) {}

  ngOnInit() {
    this.farmService.list().subscribe(
      (farms) => {
        this.farms = farms;
      },
      (error) => {
        console.log('Error fetching farms: ', error);
      }
    );
  }

  goToDetails(farm: Farm) {
    this.router.navigate(['/details', farm]);
  }
}