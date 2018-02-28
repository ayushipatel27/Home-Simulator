import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ApplianceDetailsPage } from '../appliancedetails/appliancedetails';


/**
 * Generated class for the AppliancesPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-appliances',
  templateUrl: 'appliances.html',
})
export class AppliancesPage {


  page = 1;
  perPage = 0;
  totalData = 0;
  totalPage = 0;

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  appliances = [
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

  ionViewDidLoad() {
    console.log('ionViewDidLoad AppliancesPage');
  }

  navigateToApplianceDetailsPage(appliance) {
    console.log(appliance);
    console.log('Navigating to appliance details page.');
    this.navCtrl.push('ApplianceDetailsPage', {'appliance': appliance});
    }

}
