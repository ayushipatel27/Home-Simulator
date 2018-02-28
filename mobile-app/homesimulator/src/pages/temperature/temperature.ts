import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';


@IonicPage()
@Component({
  selector: 'page-temperature',
  templateUrl: 'temperature.html',
})
export class TemperaturePage {

  temperature = 50;

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad TemperaturePage');

    //var slider = (document.getElementById("myslider") as HTMLInputElement);
    
    //var output = (document.getElementById("output"));
    //output.innerHTML = slider.value; // Display the default slider value

    //slider.oninput = function() {
    //output.innerHTML = (this as HTMLInputElement).value;

    }
    
  }

