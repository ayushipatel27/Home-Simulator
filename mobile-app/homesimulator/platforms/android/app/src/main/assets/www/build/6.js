webpackJsonp([6],{

/***/ 287:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "RoomPageModule", function() { return RoomPageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__room__ = __webpack_require__(599);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



var RoomPageModule = (function () {
    function RoomPageModule() {
    }
    RoomPageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["I" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_2__room__["a" /* RoomPage */],
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["d" /* IonicPageModule */].forChild(__WEBPACK_IMPORTED_MODULE_2__room__["a" /* RoomPage */]),
            ],
        })
    ], RoomPageModule);
    return RoomPageModule;
}());

//# sourceMappingURL=room.module.js.map

/***/ }),

/***/ 599:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return RoomPage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__providers_api_api__ = __webpack_require__(101);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



/**
 * Generated class for the RoomPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */
var RoomPage = (function () {
    function RoomPage(navCtrl, navParams, ApiProvider) {
        this.navCtrl = navCtrl;
        this.navParams = navParams;
        this.ApiProvider = ApiProvider;
        console.log(this.navParams.get('room'));
        this.room = this.navParams.get('room');
        this.id = this.room.roomid;
        console.log(this.id);
        this.name = this.room.roomname;
        console.log(this.name);
    }
    RoomPage.prototype.ionViewDidLoad = function () {
        var _this = this;
        console.log('ionViewDidLoad RoomPage');
        console.log(this.id);
        this.ApiProvider.getRoomDetails(this.id).subscribe(function (res) {
            console.log(res);
            _this.sensors = res;
        });
    };
    // navigateToApplianceDetailsPage(appliance) {
    //   console.log(appliance);
    //   console.log('Navigating to appliance details page.');
    //   this.navCtrl.push('ApplianceDetailsPage', {'appliance': appliance});
    //   }
    RoomPage.prototype.navigateToSensorDetailsPage = function (sensor) {
        console.log(sensor);
        console.log('Navigating to sensor details page.');
        this.navCtrl.push('SensorDetailsPage', { 'sensor': sensor });
    };
    RoomPage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-room',template:/*ion-inline-start:"C:\Users\Roderick\Documents\HomeSimulator\mobile-app\homesimulator\src\pages\room\room.html"*/'<ion-header>\n\n    <ion-navbar>\n      <ion-title>Room</ion-title>\n    </ion-navbar>\n  \n  </ion-header>\n  \n  \n  <ion-content class="background" padding>\n  \n    <ion-card class="rooms-card">\n      <ion-list class="rooms-list">\n        <ion-item-group>\n            <ion-item-divider class="header-divider" color="light">{{name}} Room</ion-item-divider>\n          <ion-item text-wrap *ngFor="let sensor of sensors" class="room-item" (click)="navigateToSensorDetailsPage(sensor)">\n            <ion-label>Sensor: {{sensor.sensorname}}</ion-label>\n          </ion-item>\n        </ion-item-group>\n      </ion-list>\n    </ion-card>\n  \n  </ion-content>\n  '/*ion-inline-end:"C:\Users\Roderick\Documents\HomeSimulator\mobile-app\homesimulator\src\pages\room\room.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["e" /* NavController */], __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["f" /* NavParams */], __WEBPACK_IMPORTED_MODULE_2__providers_api_api__["a" /* ApiProvider */]])
    ], RoomPage);
    return RoomPage;
}());

//# sourceMappingURL=room.js.map

/***/ })

});
//# sourceMappingURL=6.js.map