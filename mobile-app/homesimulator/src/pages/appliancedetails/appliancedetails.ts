import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ApiProvider } from '../../providers/api/api';


/**
 * Generated class for the AppliancedetailsPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-appliancedetails',
  templateUrl: 'appliancedetails.html',
})
export class ApplianceDetailsPage {

   id: number;
   data;
   name: string;
   appliance;
   powerrate;
   powerusage;
   onoffswitch: boolean = false;



  constructor(public navCtrl: NavController, public navParams: NavParams, public ApiProvider: ApiProvider) {
    console.log(this.navParams);
    this.appliance = this.navParams.data.appliance;
    console.log(this.appliance);
    this.id = this.appliance.applianceid;
    this.name = this.appliance.appliancename;
    this.powerrate = this.appliance.powerrate;
    this.powerusage = this.appliance.powerusage;
  }

  result = {'sensorname': 'guestbathroomlightsensor', 'sensorid': 8, 'applianceid': 23, 'appliancename': 'guestbathroomlight', 'poweruseage': 12, 'powerrate': 1.14, 'status': 0};


  ionViewDidLoad() {
    console.log('ionViewDidLoad AppliancedetailsPage');
    console.log(this.name);
    console.log(this.id);
  }

}
