import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { DataVisualizationPage } from './data-visualization';
import * as d3 from "d3";

@NgModule({
  declarations: [
    DataVisualizationPage,
  ],
  imports: [
    IonicPageModule.forChild(DataVisualizationPage),
  ],
})
export class DataVisualizationPageModule {}
