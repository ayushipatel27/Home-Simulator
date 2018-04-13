import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { ApplianceDetailsPage } from './appliancedetails';

@NgModule({
  declarations: [
    ApplianceDetailsPage,
  ],
  imports: [
    IonicPageModule.forChild(ApplianceDetailsPage),
  ],
})
export class AppliancedetailsPageModule {}
