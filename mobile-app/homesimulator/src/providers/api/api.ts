import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'text' })
};

@Injectable()
export class ApiProvider {

  rooms: any;
  sensors: any;
  appliances: any;
  dailyUse: any;
  hvacUse: any;
  waterUse: any;
  weather: any;
  weekPower: any;
  weekWater: any;
  monthPower: any;
  monthWater: any;


  constructor(public http: HttpClient) {
    console.log('Hello ApiProvider Provider');
  }

  getRooms() {
    return this.http.get('http://localhost:8000/api/rooms/');
  }
  getRoomDetails(id) {
    return this.http.get('http://localhost:8000/api/getsensors/' + id);
  }
  getSensorDetails(id) {
    return this.http.get('http://localhost:8000/api/getappliances/' + id);
  }
  getSensors() {
    return this.http.get('http://localhost:8000/api/sensors/');
  }
  getSensor(id) {
    return this.http.get('http://localhost:8000/api/sensors/' +id);
  }
  // getSensorDetails(id) {
  //   return this.http.get('http://localhost:8000/api/sensors/' + id);
  // }
  getAppliances() {
    return this.http.get('http://localhost:8000/api/appliances/')
  }
  getApplianceDetails(id) {
    return this.http.get('http://localhost:8000/api/appliances/' + id);
  }
  getDailyUse() {
    this.dailyUse = this.http.get('http://localhost:8000/api/rooms/');
  }
  getHvacUse() {
    this.hvacUse = this.http.get('http://localhost:8000/api/rooms/');
  }
  getWaterUse() {
    this.waterUse = this.http.get('http://localhost:8000/api/rooms/');
  }
  getWeather() {
    this.weather = this.http.get('http://localhost:8000/api/rooms/');
  }
  getWeekofUsage() {
      return this.http.get('http://localhost:8000/api/getweekofusage/');
  }
  getMonthofUsage() {
    return this.http.get('http://localhost:8000/api/getmonthofusage/');
  }
  getInProgress() {
    return this.http.get('http://localhost:8000/api/inprogress/');
  }
  getCurrentState() {
    return this.http.get('http://localhost:8000/api/gethousestate/');
  }
  postCurrentState(state) {
    console.log('Sending post request of: ' + JSON.stringify(state));
    return this.http.post('http://localhost:8000/api/update/homestate/', state as JSON, httpOptions);
  }

}

//   getRooms() {
//     return this.http.get('http://10.0.2.2:8000/api/rooms/');
//   }
//   getRoomDetails(id) {
//     return this.http.get('http://10.0.2.2:8000/api/getsensors/' + id);
//   }
//   getSensorDetails(id) {
//     return this.http.get('http://10.0.2.2:8000/api/getappliances/' + id);
//   }
//   getSensors() {
//     return this.http.get('http://10.0.2.2:8000/api/sensors/');
//   }
//   // getSensorDetails(id) {
//   //   return this.http.get('http://localhost:8000/api/sensors/' + id);
//   // }
//   getAppliances() {
//     return this.http.get('http://10.0.2.2:8000/api/appliances/')
//   }
//   getApplianceDetails(id) {
//     return this.http.get('http://10.0.2.2:8000/api/appliances/' + id);
//   }
//   getDailyUse() {
//     this.dailyUse = this.http.get('http://10.0.2.2:8000/api/rooms/');
//   }
//   getHvacUse() {
//     this.hvacUse = this.http.get('http://10.0.2.2:8000/api/rooms/');
//   }
//   getWaterUse() {
//     this.waterUse = this.http.get('http://10.0.2.2:8000/api/rooms/');
//   }
//   getWeather() {
//     this.weather = this.http.get('http://10.0.2.2:8000/api/rooms/');
//   }
//   getWeekofUsage() {
//       return this.http.get('http://10.0.2.2:8000/api/getweekofusage/');
//   }
//   getMonthofUsage() {
//     return this.http.get('http://10.0.2.2:8000/api/getmonthofusage/');
//   }
//   getInProgress() {
//     return this.http.get('http://10.0.2.2:8000/api/inprogress/');
//   }
//   getCurrentState() {
//     return this.http.get('http://10.0.2.2:8000/api/gethousestate/');
//   }
//   postCurrentState(state) {
//     console.log('Sending post request of: ' + state);
//     return this.http.post('http://10.0.2.2:8000/api/update/homestate/', state as JSON, httpOptions);
//   }

// }

