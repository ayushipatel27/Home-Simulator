import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';


@IonicPage()
@Component({
  selector: 'page-temperature',
  templateUrl: 'temperature.html',
})
export class TemperaturePage {

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad TemperaturePage');

    var slider = (<HTMLInputElement>document.getElementById("myRange"));
    var output = (<HTMLInputElement>document.getElementById("output"));
    output.innerHTML = slider.value; // Display the default slider value

  // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function() {
    output.innerHTML = this.value;
    }
    
  }

}
