import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { RoomPage } from '../room/room';
import { ApiProvider } from '../../providers/api/api';


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


  constructor(public navCtrl: NavController, public navParams: NavParams, public ApiProvider: ApiProvider) {
  }

  rooms; /** = [
    {'name': 'garage', 'id': 1},
    {'name': 'living room', 'id': 2},
    {'name': 'kitchen', 'id': 3},
    {'name': 'masterbedroom', 'id': 4},
    {'name': 'masterbathroom', 'id': 5},
    {'name': 'guestroom1', 'id': 6},
    {'name': 'guestroom2', 'id': 7},
    {'name': 'guestbathroom', 'id': 8}
  ]; **/

  ionViewDidLoad() {
    console.log('ionViewDidLoad RoomsPage');
    this.ApiProvider.getRooms().subscribe(res => {
      console.log(res)
      this.rooms = res
    })
  }

  navigateToRoomPage(room) {
    console.log(room);
    console.log('Navigating to room details page.');
    this.navCtrl.push('RoomPage', {'room': room});
    }

}
