import { Component } from '@angular/core';

import { VisualizationPage } from '../visualization/visualization';
import { ContactPage } from '../contact/contact';
import { HomePage } from '../home/home';
import { SettingsPage } from '../settings/settings';


@Component({
  templateUrl: 'tabs.html'
})
export class TabsPage {

  tab1Root = HomePage;
  tab2Root = VisualizationPage;
  tab3Root = SettingsPage;

  constructor() {

  }
}
