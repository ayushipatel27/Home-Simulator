import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { PowerVisualizationPage } from './powervisualization';
import * as d3 from "d3";
import * as Chart from "chartjs";


@NgModule({
  declarations: [
    PowerVisualizationPage,
  ],
  imports: [
    IonicPageModule.forChild(PowerVisualizationPage),
  ],
})
export class PowervisualizationPageModule {}
