import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { SensorDetailsPage } from './sensordetails';

@NgModule({
  declarations: [
    SensorDetailsPage,
  ],
  imports: [
    IonicPageModule.forChild(SensorDetailsPage),
  ],
})
export class SensordetailsPageModule {}
