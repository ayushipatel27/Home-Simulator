import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ApiProvider } from '../../providers/api/api';
import {Observable} from 'rxjs/Rx';
import * as $ from 'jquery';
import * as _ from 'lodash';


/**
 * Generated class for the AppliancedetailsPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-appliancedetails',
  templateUrl: 'appliancedetails.html',
})
export class ApplianceDetailsPage {

   id: number;
   data;
   name: string;
   appliance;
   powerrate;
   powerusage;
   onoffswitch: boolean;
   sensor;
   currentState;



  constructor(public navCtrl: NavController, public navParams: NavParams, public ApiProvider: ApiProvider) {
    console.log(this.navParams);
    this.appliance = this.navParams.data.appliance;
    console.log(this.appliance);
    this.id = this.appliance.applianceid;
    this.name = this.appliance.appliancename;
    this.powerrate = this.appliance.powerrate;
    this.powerusage = this.appliance.powerusage;
    this.ApiProvider.getSensor(this.id).subscribe((res: any) => {
      this.sensor = res;
      console.log('The sensor state is: ' + this.sensor.sensorstate);
     if(this.sensor.sensorstate == 0) {
       this.onoffswitch = false;
     } else {
       this.onoffswitch = true;
     }
    })
    this.ApiProvider.getCurrentState().subscribe(res => {
      console.log(res);
      this.currentState = res;
    })
  }


  ionViewDidLoad() {
    console.log('ionViewDidLoad AppliancedetailsPage');
    console.log(this.name);
    console.log(this.id);
    console.log(this.onoffswitch);
  }


  sendState() {
    console.log('Sending State');
    console.log('The onoffswitch is st to: ' + this.onoffswitch);
    var now = new Date(),
      nowformat = [now.getFullYear(),
        now.getMonth() + 1,
        now.getDate()
      ].join('-') + ' ' + [now.getHours(),
        now.getMinutes(),
        now.getSeconds()
      ].join(':');
    this.currentState.home.hvacusage.endtimestamp = nowformat;
    this.currentState.home.powerusage.endtimestamp = nowformat;
    this.currentState.home.waterusage.endtimestamp = nowformat;

    var page = this;
    var newpage;
    console.log(page);
    console.log('This sensor is on or open: ' + this.onoffswitch);
    if (this.onoffswitch == true) {
      console.log('About to turn something on.');
      turnOn(page).then((newpage: any) => {
        console.log('Entered then promise');
        this.ApiProvider.postCurrentState(newpage.currentState).subscribe(data => {
          return true;
        }, error => {
          console.log("Error posting state.");
          console.log(error);
          return Observable.throw(error);
        })
      })
    } else {
      console.log('About to turn something off.');
      //newpage = turnOff(page);
      turnOff(page).then((newpage: any) => {
        console.log('Entered then promise');
        this.ApiProvider.postCurrentState(newpage.currentState).subscribe(data => {
          return true;
        }, error => {
          console.log("Error posting state.");
          console.log(error);
          return Observable.throw(error);
        })
      })
    }
  }

  }

  function turnOn(page: any) {
    console.log(page);
    return new Promise((resolve, reject) => {
      console.log(page);
      console.log(page.id);
      var waterids = [19, 20, 23, 24, 42, 44];
      var hvacid = 36;
      if (waterids.includes(page.id)) {
        try {
          console.log('The currently on waterids are: ' + page.currentState.home.waterusage.sensorids);
          let arr = JSON.parse(page.currentState.home.waterusage.sensorids);
          let arr2 = JSON.parse(page.currentState.home.powerusage.sensorids)
          let arr3 = JSON.parse(page.currentState.home.hvacusage.sensorid)
          arr.push(page.id);
          page.currentState.home.waterusage.sensorids = arr;
          page.currentState.home.powerusage.sensorids = arr2;
          page.currentState.home.hvacusage.sensorid = arr3;
          console.log('Turned on ' + JSON.stringify(page.currentState.home.waterusage));
        }catch(e) {
          page.currentState.home.waterusage.sensoridspush(page.id);
          console.log('Turned on ' + JSON.stringify(page.currentState.home.waterusage));
        }
        resolve(page)
      }
      if (page.id == hvacid) {
        try {
          let arr = JSON.parse(page.currentState.home.hvacusage.sensorid);
          let arr2 = JSON.parse(page.currentState.home.powerusage.sensorids);
          let arr3 = JSON.parse(page.currentState.home.waterusage.sensorid);
          arr.push(page.id);
          console.log(arr);
          page.currentState.home.hvacusage.sensorid = arr;
          page.currentState.home.powerusage.sensorids = arr2;
          page.currentState.home.waterusage.sensorids = arr3;
        }catch(e) {
          page.currentState.home.hvacusage.sensorid.push(page.id);
        }
        resolve(page);
      }
      if (!waterids.includes(page.id) && hvacid != page.id) {
        try{
          let arr = JSON.parse(page.currentState.home.powerusage.sensorids);
          let arr2 = JSON.parse(page.currentState.home.waterusage.sensorids);
          let arr3 = JSON.parse(page.currentState.home.hvacusage.sensorid);
          console.log('The currently on powerids are: ' + page.currentState.home.powerusage.sensorids);
          arr.push(page.id);
          page.currentState.home.powerusage.sensorids = arr;
          page.currentState.home.waterusage.sensorids = arr2;
          page.currentState.home.hvacusage.sensorids = arr3;
        }catch(e) {
          page.currentState.home.powerusage.sensorids.push(page.id);
        }
        console.log('Turned on ' + JSON.stringify(page.currentState.home.powerusage));
        resolve(page);
      }
    });
  }

  function turnOff(page: any) {
    return new Promise((resolve, reject) => {
      console.log(page);
      console.log(page.id);
      var waterids = [19, 20, 23, 24, 42, 44];
      var hvacid = 36;

      if (waterids.includes(page.id)) {
        console.log('Entered if');
        try {
        let arr = JSON.parse(page.currentState.home.waterusage.sensorids);
        let arr2 = JSON.parse(page.currentState.home.powerusage.sensorids);
        let arr3 = JSON.parse(page.currentState.home.hvacusage.sensorid);
        _.pull(arr, page.id);
        page.currentState.home.waterusage.sensorids = arr;
        page.currentState.home.powerusage.sensorids = arr2;
        page.currentState.home.hvacusage.sensorid = arr3;
        console.log(page.currentState.home.waterusage.sensorids);
        }catch(e) {
          _.pull(page.currentState.home.waterusage.sensorids, page.id);
        }        
        resolve(page);
      }
      if (page.id == hvacid) {
        console.log('Entered if');
        try{
          let arr = JSON.parse(page.currentState.home.hvacusage.sensorid);
          let arr2 = JSON.parse(page.currentState.home.powerusage.sensorids)
          let arr3 = JSON.parse(page.currentState.home.waterusage.sensorid)
          _.pull(arr, page.id);
          page.currentState.home.hvacusage.sensorid = arr;
          page.currentState.home.powerusage.sensorids = arr2;
          page.currentState.home.waterusage.sensorids = arr3;
        }catch(e) {
          _.pull(page.currentState.home.hvacusage.sensorid, page.id);
        }
        console.log(page.currentState.home.hvacusage.sensorids);
        resolve(page);
      }
      if (!waterids.includes(page.id) && hvacid != page.id) {
        console.log('Entered if');
        try {
        let arr = JSON.parse(page.currentState.home.powerusage.sensorids);
        let arr2 = JSON.parse(page.currentState.home.waterusage.sensorids);
        let arr3 = JSON.parse(page.currentState.home.hvacusage.sensorid);
        _.pull(arr, page.id);
        page.currentState.home.powerusage.sensorids = arr;
        page.currentState.home.waterusage.sensorids = arr2;
        page.currentState.home.hvacusage.sensorids = arr3;
        }catch(e) {
          _.pull(page.currentState.home.powerusage.sensorids, page.id);
        }
        console.log(page.currentState.home.powerusage.sensorids);
        resolve(page);
      }
      console.log('Turned off ' + JSON.stringify(page.currentState.home.powerusage));
    })
  }

