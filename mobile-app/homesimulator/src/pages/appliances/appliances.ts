import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ApplianceDetailsPage } from '../appliancedetails/appliancedetails';
import { ApiProvider } from '../../providers/api/api';



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
  //appliances;

  constructor(public navCtrl: NavController, public navParams: NavParams, public ApiProvider: ApiProvider) {
  }

  appliances;

  ionViewDidLoad() {
    console.log('ionViewDidLoad AppliancesPage');
    this.ApiProvider.getAppliances().subscribe(res => {
      console.log(res)
      this.appliances = res
    });
    console.log(this.appliances);
  }

  navigateToApplianceDetailsPage(appliance) {
    console.log(appliance);
    console.log('Navigating to appliance details page.');
    this.navCtrl.push('ApplianceDetailsPage', {'appliance': appliance});
    }

}
