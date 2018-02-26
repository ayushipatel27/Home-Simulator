import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

/**
 * Generated class for the RoomsPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */


@IonicPage()
@Component({
  selector: 'page-rooms',
  templateUrl: 'rooms.html',
})
export class RoomsPage {


  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  rooms = [
    {'name': 'kitchen', 'id': 1},
    {'name': 'living room', 'id': 2},
    {'name': 'kitchen', 'id': 3},
    {'name': 'masterbedroom', 'id': 4},
    {'name': 'masterbathroom', 'id': 5},
    {'name': 'guestroom1', 'id': 6},
    {'name': 'guestroom2', 'id': 7},
    {'name': 'guestbathroom', 'id': 8}
  ];

  ionViewDidLoad() {
    console.log('ionViewDidLoad RoomsPage');
  }

  navigateToModule() {
    console.log('Navigating to module page.');
    //this.navCtrl.push('RoomsPage');
    }

}
