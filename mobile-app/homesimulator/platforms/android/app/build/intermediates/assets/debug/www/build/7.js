webpackJsonp([7],{

/***/ 285:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "InProgressPageModule", function() { return InProgressPageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__in_progress__ = __webpack_require__(597);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



var InProgressPageModule = (function () {
    function InProgressPageModule() {
    }
    InProgressPageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["I" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_2__in_progress__["a" /* InProgressPage */],
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["d" /* IonicPageModule */].forChild(__WEBPACK_IMPORTED_MODULE_2__in_progress__["a" /* InProgressPage */]),
            ],
        })
    ], InProgressPageModule);
    return InProgressPageModule;
}());

//# sourceMappingURL=in-progress.module.js.map

/***/ }),

/***/ 597:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return InProgressPage; });
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



var InProgressPage = (function () {
    function InProgressPage(navCtrl, navParams, ApiProvider) {
        var _this = this;
        this.navCtrl = navCtrl;
        this.navParams = navParams;
        this.ApiProvider = ApiProvider;
        this.ApiProvider.getInProgress().subscribe(function (res) {
            console.log(res);
            _this.inprogress = res;
        });
    }
    InProgressPage.prototype.ionViewDidLoad = function () {
        console.log('ionViewDidLoad InProgressPage');
    };
    InProgressPage.prototype.navigateToSensorDetailsPage = function (sensor) {
        console.log(sensor);
        console.log('Navigating to sensor details page.');
        this.navCtrl.push('SensorDetailsPage', { 'sensor': sensor });
    };
    InProgressPage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-in-progress',template:/*ion-inline-start:"C:\Users\Roderick\Documents\HomeSimulator\mobile-app\homesimulator\src\pages\in-progress\in-progress.html"*/'<ion-header>\n\n\n\n  <ion-navbar>\n\n    <ion-title>in-progress</ion-title>\n\n  </ion-navbar>\n\n\n\n</ion-header>\n\n\n\n\n\n<ion-content class="background" padding>\n\n\n\n  <ion-card class="rooms-card">\n\n\n\n    <ion-scroll scrollY="true">\n\n\n\n      <ion-list class="rooms-list">\n\n        <ion-item-group>\n\n          <ion-item-divider class="header-divider" color="light">In Progress</ion-item-divider>\n\n          <ion-item text-wrap *ngFor="let sensor of inprogress" class="room-item" (click)="navigateToSensorDetailsPage(sensor)">\n\n            Sensor: {{sensor.sensorname}}\n\n          </ion-item>\n\n        </ion-item-group>\n\n      </ion-list>\n\n    </ion-scroll>\n\n    <!--<ion-infinite-scroll (ionInfinite)="doInfinite($event)">\n\n      <ion-infinite-scroll-content></ion-infinite-scroll-content>\n\n    </ion-infinite-scroll> -->\n\n\n\n  </ion-card>\n\n\n\n</ion-content>\n\n'/*ion-inline-end:"C:\Users\Roderick\Documents\HomeSimulator\mobile-app\homesimulator\src\pages\in-progress\in-progress.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["e" /* NavController */], __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["f" /* NavParams */], __WEBPACK_IMPORTED_MODULE_2__providers_api_api__["a" /* ApiProvider */]])
    ], InProgressPage);
    return InProgressPage;
}());

//# sourceMappingURL=in-progress.js.map

/***/ })

});
//# sourceMappingURL=7.js.map