import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { InProgressPage } from './in-progress';

@NgModule({
  declarations: [
    InProgressPage,
  ],
  imports: [
    IonicPageModule.forChild(InProgressPage),
  ],
})
export class InProgressPageModule {}
