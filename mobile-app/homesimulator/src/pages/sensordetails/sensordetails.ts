import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ApiProvider } from '../../providers/api/api';

/**
 * Generated class for the SensordetailsPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-sensordetails',
  templateUrl: 'sensordetails.html',
})
export class SensorDetailsPage {

  id: number;
  data;
  name: string;
  sensor;
  appliance;
  powerrate;
  powerusage;
  onoffswitch: boolean = false;
  onoropen: boolean = false;



 constructor(public navCtrl: NavController, public navParams: NavParams, public ApiProvider: ApiProvider) {
   console.log(this.navParams);
   this.sensor = this.navParams.data.sensor;
   this.id = this.sensor.sensorid;
   this.name = this.sensor.sensorname;
   this.ApiProvider.getSensorDetails(this.id).subscribe(res => {
    console.log(res);
    this.appliance = res[0];
    this.powerrate = this.appliance.powerrate;
    this.powerusage = this.appliance.powerusage;
    // console.log('The appliance is: ' + this.appliance.appliancename);
    // console.log('The appliance powerrate is: ' + this.appliance.powerrate);
  })
   console.log('The sensor state is: ' + this.sensor.sensorstate);
   if(this.sensor.sensorstate == 0) {
     this.onoffswitch = false;
   } else {
     this.onoffswitch = true;
   }
 }

 ionViewDidLoad() {
   console.log('ionViewDidLoad AppliancedetailsPage');
   console.log(this.name);
   console.log(this.id);
 }


}
