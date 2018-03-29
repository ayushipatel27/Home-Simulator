import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { WaterVisualizationPage } from './watervisualization';

@NgModule({
  declarations: [
    WaterVisualizationPage,
  ],
  imports: [
    IonicPageModule.forChild(WaterVisualizationPage),
  ],
})
export class WatervisualizationPageModule {}
