import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ApplianceDetailsPage } from '../appliancedetails/appliancedetails';


/**
 * Generated class for the InProgressPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-in-progress',
  templateUrl: 'in-progress.html',
})
export class InProgressPage {

  inprogress = [
    {'sensorname': 'kitchenlightsensor', 'sensorid': 1, 'applianceid': 1, 'appliancename': 'kitchenlight1', 'poweruseage': 20, 'powerrate': 1.40},
    {'sensorname': 'kitchenlightsensor', 'sensorid': 1, 'applianceid': 4, 'appliancename': 'kitchenlight3', 'poweruseage': 23, 'powerrate': 1.40},
    {'sensorname': 'kitchenappliancesensor', 'sensorid': 3, 'applianceid': 6, 'appliancename': 'oven', 'poweruseage': 34, 'powerrate': 1.70},
    {'sensorname': 'kitchenappliancesensor', 'sensorid': 3, 'applianceid': 7, 'appliancename': 'refrigerator', 'poweruseage': 40, 'powerrate': 1.93},
    {'sensorname': 'guestbathroomlightsensor', 'sensorid': 8, 'applianceid': 23, 'appliancename': 'guestbathroomlight', 'poweruseage': 12, 'powerrate': 1.14},
    {'sensorname': 'guestbathroomwatersensor', 'sensorid': 9, 'applianceid': 26, 'appliancename': 'guestbathroomfaucet', 'wateruseage': 3.0, 'waterrate': 1.95},
    {'sensorname': 'kitchenlightsensor', 'sensorid': 1, 'applianceid': 1, 'appliancename': 'kitchenlight1', 'poweruseage': 20, 'powerrate': 1.40},
    {'sensorname': 'kitchenlightsensor', 'sensorid': 1, 'applianceid': 4, 'appliancename': 'kitchenlight3', 'poweruseage': 23, 'powerrate': 1.40},
    {'sensorname': 'kitchenappliancesensor', 'sensorid': 3, 'applianceid': 6, 'appliancename': 'oven', 'poweruseage': 34, 'powerrate': 1.70},
    {'sensorname': 'kitchenappliancesensor', 'sensorid': 3, 'applianceid': 7, 'appliancename': 'refrigerator', 'poweruseage': 40, 'powerrate': 1.93},
    {'sensorname': 'guestbathroomlightsensor', 'sensorid': 8, 'applianceid': 23, 'appliancename': 'guestbathroomlight', 'poweruseage': 12, 'powerrate': 1.14},
    {'sensorname': 'guestbathroomwatersensor', 'sensorid': 9, 'applianceid': 26, 'appliancename': 'guestbathroomfaucet', 'wateruseage': 3.0, 'waterrate': 1.95},
    {'sensorname': 'kitchenlightsensor', 'sensorid': 1, 'applianceid': 1, 'appliancename': 'kitchenlight1', 'poweruseage': 20, 'powerrate': 1.40},
    {'sensorname': 'kitchenlightsensor', 'sensorid': 1, 'applianceid': 4, 'appliancename': 'kitchenlight3', 'poweruseage': 23, 'powerrate': 1.40},
    {'sensorname': 'kitchenappliancesensor', 'sensorid': 3, 'applianceid': 6, 'appliancename': 'oven', 'poweruseage': 34, 'powerrate': 1.70},
    {'sensorname': 'kitchenappliancesensor', 'sensorid': 3, 'applianceid': 7, 'appliancename': 'refrigerator', 'poweruseage': 40, 'powerrate': 1.93},
    {'sensorname': 'guestbathroomlightsensor', 'sensorid': 8, 'applianceid': 23, 'appliancename': 'guestbathroomlight', 'poweruseage': 12, 'powerrate': 1.14},
    {'sensorname': 'guestbathroomwatersensor', 'sensorid': 9, 'applianceid': 26, 'appliancename': 'guestbathroomfaucet', 'wateruseage': 3.0, 'waterrate': 1.95},
    {'sensorname': 'kitchenlightsensor', 'sensorid': 1, 'applianceid': 1, 'appliancename': 'kitchenlight1', 'poweruseage': 20, 'powerrate': 1.40},
    {'sensorname': 'kitchenlightsensor', 'sensorid': 1, 'applianceid': 4, 'appliancename': 'kitchenlight3', 'poweruseage': 23, 'powerrate': 1.40},
    {'sensorname': 'kitchenappliancesensor', 'sensorid': 3, 'applianceid': 6, 'appliancename': 'oven', 'poweruseage': 34, 'powerrate': 1.70},
    {'sensorname': 'kitchenappliancesensor', 'sensorid': 3, 'applianceid': 7, 'appliancename': 'refrigerator', 'poweruseage': 40, 'powerrate': 1.93},
    {'sensorname': 'guestbathroomlightsensor', 'sensorid': 8, 'applianceid': 23, 'appliancename': 'guestbathroomlight', 'poweruseage': 12, 'powerrate': 1.14},
    {'sensorname': 'guestbathroomwatersensor', 'sensorid': 9, 'applianceid': 26, 'appliancename': 'guestbathroomfaucet', 'wateruseage': 3.0, 'waterrate': 1.95},
  ];


  constructor(public navCtrl: NavController, public navParams: NavParams) {
    //for (let i = 0; i < 30; i++) {
      //this.inprogress.push(this.inprogress.length);
    //}
  }


  doInfinite(infiniteScroll) {
    console.log('Begin async operation');

    setTimeout(() => {
      //API call


      console.log('Async operation has ended');
      infiniteScroll.complete();
    }, 500);
  }

  
  ionViewDidLoad() {
    console.log('ionViewDidLoad InProgressPage');
  }

  navigateToModule() {
    console.log('Navigating to module page.');
    //this.navCtrl.push('RoomsPage');
    }

  navigateToApplianceDetailsPage(appliance) {
    console.log(appliance);
    console.log('Navigating to appliance details page.');
    this.navCtrl.push('ApplianceDetailsPage', {'appliance': appliance});
    }

}
