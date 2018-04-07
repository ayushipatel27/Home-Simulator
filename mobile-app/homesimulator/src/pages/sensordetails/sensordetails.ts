import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ApiProvider } from '../../providers/api/api';
import { HttpClient } from '@angular/common/http';
import * as $ from 'jquery';
import * as _ from 'lodash';

/**
 * Generated class for the SensordetailsPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-sensordetails',
  templateUrl: 'sensordetails.html',
})
export class SensorDetailsPage {

  id: number;
  data;
  name: string;
  sensor;
  appliance;
  powerrate;
  powerusage;
  onoffswitch: boolean = false;
  onoropen: boolean = false;
  currentState;


 constructor(public navCtrl: NavController, public navParams: NavParams, public ApiProvider: ApiProvider) {
   console.log(this.navParams);
   this.sensor = this.navParams.data.sensor;
   this.id = this.sensor.sensorid;
   this.name = this.sensor.sensorname;
   this.ApiProvider.getSensorDetails(this.id).subscribe(res => {
    console.log(res);
    this.appliance = res[0];
    this.powerrate = this.appliance.powerrate;
    this.powerusage = this.appliance.powerusage;
    // console.log('The appliance is: ' + this.appliance.appliancename);
    // console.log('The appliance powerrate is: ' + this.appliance.powerrate);
  })
  this.ApiProvider.getCurrentState().subscribe(res => {
    console.log(res);
    this.currentState = res;
  })
   console.log('The sensor state is: ' + this.sensor.sensorstate);
   if(this.sensor.sensorstate == 0) {
     this.onoffswitch = false;
   } else {
     this.onoffswitch = true;
   }
 }

 ionViewDidLoad() {
   console.log('ionViewDidLoad AppliancedetailsPage');
   console.log(this.name);
   console.log(this.id);
 }

 sendState() {
  console.log('Sending State');
  var now = new Date();
  this.currentState.home.hvacusage.endtimestamp = now;
  this.currentState.home.powerusage.endtimestamp = now;
  this.currentState.home.waterusage.endtimestamp = now;

  var page = {id: this.id, currentState: this.currentState, onoropen: this.onoropen};

  console.log(now);
  let po;
  let wa;

  var usagefunction = function(page) {
    alert("here");
    console.log(page);
    var prom = new Promise(function(resolve, reject) {
      console.log(page);
    });
    return prom;
  };
  var cWat = function(page){
    console.log('page' + page);
    var promise = new Promise(function(resolve, reject){
      wa = calculateWater(page.currentState);
      console.log(wa);
    });
    return promise;
  };
  var cPow = function(page){
    console.log('page' + page)
    var promise = new Promise(function(resolve, reject){
      po = calculatePower(page.currentState);
      console.log(po);
    });
    return promise;
  };

  usagefunction(page).then(cPow(page)).then(cWat(page));
  console.log('after calls');
  //    console.log("Entered then promise.");
  console.log(page.currentState.home.powerusage);
  console.log(page.currentState.home.waterusage);
  // uageF().calculatePower().calculateWater();
}

 //
 //  sendState().then((page: JSON) => {
 //    console.log("Entered then promise.");
 //    // console.log(page.currentState.home.powerusage);
 //    // console.log(page.currentState.home.waterusage);
 //    if(page.onoropen == true) {
 //      turnOn(page);
 //      return page;
 //    }else {
 //      turnOff(page);
 //      return page;
 //    }
 //  }, function(err) {
 //    console.log(err); // Error: "It broke"
 //  })
 //  .then(function(page) {
 //    console.log('The page before post is: ' + JSON.stringify(page));
 //    this.http.post('http://localhost:8000/api/update/housestate/');
 //  });
 // }

//  turnOn(id) {
//   var waterids = [19,20,23,24,42,44];
//   var hvacid = 36;
//   if(waterids.includes(id)) {
//     this.currentState.home.waterusage.sensorids.push(id);
//   }
//   if(id = hvacid) {
//     this.currentState.home.hvacusage.sensorids.push(id);
//   }
//   if(!waterids.includes(id) && !hvacid == id) {
//     this.currentState.home.powerusage.sensorids.push(id);
//   }
//   console.log('Turned on ' + JSON.stringify(this.currentState.home.powerusage));

 }
//  turnOff(id) {
//   var waterids = [19,20,23,24,42,44];
//   var hvacid = [36];

//   if(waterids.includes(id)) {
//     _.pull(this.currentState.home.waterusage.sensorids, id);
//     console.log(this.currentState.home.waterusage.sensorids);
//     // console.log(this.currentState.home.waterusage.sensorids.indexOf(id));
//     // var index = this.currentState.home.waterusage.sensorids.indexOf(id);
//     // if (index !== -1) {
//     //     this.currentState.home.waterusage.sensorids.splice(index, 1);
//     // }
//   }
//   if(id == hvacid) {
//     _.pull(this.currentState.home.hvacusage.sensorids, id);
//     console.log(this.currentState.home.hvacusage.sensorids);
//     // console.log(this.currentState.home.hvacusage.sensorids.indexOf(id));
//     // var index = this.currentState.home.hvacusage.sensorids.indexOf(id);
//     // if (index !== -1) {
//     //     this.currentState.home.hvacusage.sensorids.splice(index, 1);
//     // }
//   }
//   if(!waterids.includes(id) && !hvacid == id) {
//     _.pull(this.currentState.home.powerusage.sensorids, id);
//     console.log(this.currentState.home.powerusage.sensorids);
//     // console.log(this.currentState.home.powerusage.sensorids.indexOf(id));
//     // var index = this.currentState.home.powerusage.sensorids.indexOf(id);
//     // if (index !== -1) {
//     //     this.currentState.home.powerusage.sensorids.splice(index, 1);
//     // }
//   }
//   console.log('Turned off ' + JSON.stringify(this.currentState.home.powerusage));
//  }

//  calculatePower() {
//   var cost = 0.0;
//   var usage = 0.0;
//   var now = new Date();
//   var ids = JSON.parse(this.currentState.home.powerusage.sensorids);
//   var pasttime = Date.parse(this.currentState.home.powerusage.timestamp);
//   console.log(ids);
//   ids.forEach(element => {
//      let appliance;
//      let link = 'http://localhost:8000/api/getappliances/' + element;
//      $.get(link, function(data){
//      console.log(data);
//      appliance = data[0];
//      var interval = (now.getTime() - pasttime)/1000;
//      console.log("The interval between start and finish is: " + interval +" seconds.");
//      console.log("The appliance's powerrate is: " + appliance.powerrate);
//      cost += Math.abs(calculatePowerCost(appliance.powerusage, interval));
//      usage += Math.abs(calculatePowerUsage(appliance.powerusage, interval));
//      console.log('The power cost is currently: $' + cost);
//      console.log('The power usage is currently: ' + usage + " kilowatts.");
//     });
//    });
//    this.currentState.home.powerusage.cost = cost;
//    console.log(cost);
//  }

//  calculateWater() {
//   var cost = 0.0;
//   var usage = 0.0;
//   var now = new Date();
//   var ids = JSON.parse(this.currentState.home.waterusage.sensorids);
//   var pasttime = Date.parse(this.currentState.home.waterusage.timestamp);
//   console.log(ids);
//   ids.forEach(element => {
//      let appliance;
//      let link = 'http://localhost:8000/api/getappliances/' + element;
//      $.get(link, function(data){
//      console.log(data);
//      appliance = data[0];
//      var interval = (now.getTime() - pasttime)/1000;
//      console.log("The interval between start and finish is: " + interval +" seconds.");
//      console.log("The appliance's waterusage is: " + getGallons(appliance));
//      cost += Math.abs(calculateWaterCost(appliance));
//      usage += Math.abs(getGallons(appliance));
//      console.log('The water cost is currently: $' + cost);
//      console.log('The water usage is currently: ' + usage + ' gallons');
//     });
//    });
//    this.currentState.home.waterusage.cost = cost;
//    this.currentState.home.waterusage.usage = usage;
//    //console.log(cost);
//  }


function turnOn(page) {
  var waterids = [19,20,23,24,42,44];
  var hvacid = 36;
  if(waterids.includes(page.id)) {
    page.currentState.home.waterusage.sensorids.push(page.id);
  }
  if(page.id = hvacid) {
    page.currentState.home.hvacusage.sensorids.push(page.id);
  }
  if(!waterids.includes(page.id) && !hvacid == page.id) {
    page.currentState.home.powerusage.sensorids.push(page.id);
  }
  console.log('Turned on ' + JSON.stringify(page.currentState.home.powerusage));
}

function turnOff(page) {
  var waterids = [19,20,23,24,42,44];
  var hvacid = [36];

  if(waterids.includes(page.id)) {
    _.pull(this.currentState.home.waterusage.sensorids, page.id);
    console.log(page.currentState.home.waterusage.sensorids);
    // console.log(this.currentState.home.waterusage.sensorids.indexOf(id));
    // var index = this.currentState.home.waterusage.sensorids.indexOf(id);
    // if (index !== -1) {
    //     this.currentState.home.waterusage.sensorids.splice(index, 1);
    // }
  }
  if(page.id == hvacid) {
    _.pull(this.currentState.home.hvacusage.sensorids, page.id);
    console.log(page.currentState.home.hvacusage.sensorids);
    // console.log(this.currentState.home.hvacusage.sensorids.indexOf(id));
    // var index = this.currentState.home.hvacusage.sensorids.indexOf(id);
    // if (index !== -1) {
    //     this.currentState.home.hvacusage.sensorids.splice(index, 1);
    // }
  }
  if(!waterids.includes(page.id) && !hvacid == page.id) {
    _.pull(page.currentState.home.powerusage.sensorids, page.id);
    console.log(page.currentState.home.powerusage.sensorids);
    // console.log(this.currentState.home.powerusage.sensorids.indexOf(id));
    // var index = this.currentState.home.powerusage.sensorids.indexOf(id);
    // if (index !== -1) {
    //     this.currentState.home.powerusage.sensorids.splice(index, 1);
    // }
  }
  console.log('Turned off ' + JSON.stringify(page.currentState.home.powerusage));
 }


function calculatePower(currentState)
  return new Promise(function(resolve, reject) {
  var cost = 0.0;
  var usage = 0.0;
  var now = new Date();
  var ids = JSON.parse(currentState.home.powerusage.sensorids);
  var pasttime = Date.parse(currentState.home.powerusage.timestamp);
  console.log(ids);
  ids.forEach(element => {
     let appliance;
     let link = 'http://localhost:8000/api/getappliances/' + element;
     $.get(link, function(data){
     console.log(data);
     appliance = data[0];
     var interval = (now.getTime() - pasttime)/1000;
     console.log("The interval between start and finish is: " + interval +" seconds.");
     console.log("The appliance's powerrate is: " + appliance.powerrate);
     cost += Math.abs(calculatePowerCost(appliance.powerusage, interval));
     usage += Math.abs(calculatePowerUsage(appliance.powerusage, interval));
     console.log('The power cost is currently: $' + cost);
     console.log('The power usage is currently: ' + usage + " kilowatts.");

     })
    });
    var power = {powercost: cost, powerusage: usage};
    resolve(power);
   });
 }

 function calculateWater(currentState) {
  return new Promise(function(resolve, reject) {
  var cost = 0.0;
  var usage = 0.0;
  var now = new Date();
  var ids = JSON.parse(currentState.home.waterusage.sensorids);
  var pasttime = Date.parse(currentState.home.waterusage.timestamp);
  console.log(ids);
  ids.forEach(element => {
     let appliance;
     let link = 'http://localhost:8000/api/getappliances/' + element;
     $.get(link, function(data){
     console.log(data);
     appliance = data[0];
     var interval = (now.getTime() - pasttime)/1000;
     console.log("The interval between start and finish is: " + interval +" seconds.");
     console.log("The appliance's waterusage is: " + getGallons(appliance));
     cost += Math.abs(calculateWaterCost(appliance));
     usage += Math.abs(getGallons(appliance));
     console.log('The water cost is currently: $' + cost);
     console.log('The water usage is currently: ' + usage + ' gallons');
     })
    });
    currentState.home.waterusage.cost = cost;
    currentState.home.waterusage.usage = usage;
    var water = {watercost: cost, waterusage: usage};
    resolve(water);
   });
 }

function calculatePowerCost(watts, time) {
  return ((watts * (time / 3600)) / 1000) * .12 // returns $ for kilowatts per hour
}

function calculatePowerUsage(watts, time) {
  var convertedtime = time/3600;
  var currentusage = ((watts / 1000)*convertedtime); // returns kilowatts per hour
  console.log(currentusage);
  return currentusage;
}
function calculateWaterCost(appliance) {
  var timeHotWaterUsed = getGallons(appliance) * getHotWaterPercentage(appliance) * 240;
  return calculatePowerCost(4500, timeHotWaterUsed);
}

function getGallons(appliance) {
  console.log(appliance);
  console.log(appliance.appliancename);
  if (appliance.appliancename == "Bath")
    return 30
  if (appliance.appliancename == "Shower")
    return 25
  if (appliance.appliancename == "Dishwasher")
    return 6
  if (appliance.appliancename == "Clothes Washer")
    return 20
  else
    return 0
}


function getHotWaterPercentage(appliance) {
  if (appliance.appliancename == "Bath")
    return 0.65
  if (appliance.appliancename == "Shower")
    return 0.65
  if (appliance.appliancename == "Dishwasher")
    return 1.00
  if (appliance.appliancename == "Clothes Washer")
    return 0.85
  else {
    return 0
  }
}
