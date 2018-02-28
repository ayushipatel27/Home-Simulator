import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

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
   onoffswitch: boolean = false;



  constructor(public navCtrl: NavController, public navParams: NavParams) {
    //this.id = this.navParams.get('id');
    console.log(this.navParams);
    //this.data = this.navParams.data;
    this.appliance = this.navParams.data.appliance;
    this.id = this.appliance.applianceid;
    this.name = this.appliance.appliancename;
    //this.id = this.navParams.get('applianceid');

  }

  result = {'sensorname': 'guestbathroomlightsensor', 'sensorid': 8, 'applianceid': 23, 'appliancename': 'guestbathroomlight', 'poweruseage': 12, 'powerrate': 1.14, 'status': 0};


  ionViewDidLoad() {
    console.log('ionViewDidLoad AppliancedetailsPage');
    console.log(this.name);
    console.log(this.id);
  }

}
