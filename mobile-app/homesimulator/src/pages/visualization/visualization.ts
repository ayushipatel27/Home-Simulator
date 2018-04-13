import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { PowerVisualizationPage } from '../powervisualization/powervisualization';
import { WaterVisualizationPage } from '../watervisualization/watervisualization';
import { HvacvisualizationPage } from '../hvacvisualization/hvacvisualization';

import { ApiProvider } from '../../providers/api/api';


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
  navigateToHVACVisualizationPage(){
    console.log('Navigating to HVAC Visualization Page.');
    this.navCtrl.push('HvacvisualizationPage');
  }



}
