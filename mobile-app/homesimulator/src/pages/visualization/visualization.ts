import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { PowerVisualizationPage } from '../powervisualization/powervisualization';
import { WaterVisualizationPage } from '../watervisualization/watervisualization';
import { ApiProvider } from '../../providers/api/api';


/**
 * Generated class for the VisualizationPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-visualization',
  templateUrl: 'visualization.html',
})
export class VisualizationPage {

  constructor(public navCtrl: NavController, public navParams: NavParams, public ApiProvider: ApiProvider) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad VisualizationPage');
  }

  navigateToPowerVisualizationPage() {
    console.log('Navigating to Power Visualization Page.');
    this.navCtrl.push('PowerVisualizationPage');
    }

    navigateToWaterVisualizationPage() {
      console.log('Navigating to Water Visualization Page.');
      this.navCtrl.push('WaterVisualizationPage');
      }

}
