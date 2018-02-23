import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { RoomsPage } from '../rooms/rooms';
import { InProgressPage } from '../in-progress/in-progress';
import { TemperaturePage } from '../temperature/temperature';
import { AppliancesPage } from '../appliances/appliances';


@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {

  constructor(public navCtrl: NavController) {

  }
   navigateToRoomsPage() {
    console.log('Navigating to rooms page.');
    this.navCtrl.push('RoomsPage');
    }
    navigateToAppliancesPage() {
      console.log('Navigating to appliances page.');
      this.navCtrl.push('AppliancesPage');
      }
    navigateToInProgressPage() {
      console.log('Navigating to in progress page.');
      this.navCtrl.push('InProgressPage');
    }
    navigateToTemperaturePage() {
      console.log('Navigating to temperature page.');
      this.navCtrl.push('TemperaturePage');
      }

}

