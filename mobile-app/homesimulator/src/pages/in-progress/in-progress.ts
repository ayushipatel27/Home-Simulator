import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { SensorDetailsPage } from '../sensordetails/sensordetails';
import { ApiProvider } from '../../providers/api/api';


@IonicPage()
@Component({
  selector: 'page-in-progress',
  templateUrl: 'in-progress.html',
})
export class InProgressPage {

  inprogress;

  constructor(public navCtrl: NavController, public navParams: NavParams, public ApiProvider: ApiProvider) {
    this.ApiProvider.getInProgress().subscribe(res => {
      console.log(res);
      this.inprogress = res;
    })


  }
  
  ionViewDidLoad() {
    console.log('ionViewDidLoad InProgressPage');
  }

  navigateToSensorDetailsPage(sensor) {
      console.log(sensor);
      console.log('Navigating to sensor details page.');
      this.navCtrl.push('SensorDetailsPage', {'sensor': sensor});
    }

}
