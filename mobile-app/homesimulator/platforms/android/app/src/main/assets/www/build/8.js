webpackJsonp([8],{

/***/ 283:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppliancesPageModule", function() { return AppliancesPageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__appliances__ = __webpack_require__(595);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



var AppliancesPageModule = (function () {
    function AppliancesPageModule() {
    }
    AppliancesPageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["I" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_2__appliances__["a" /* AppliancesPage */],
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["d" /* IonicPageModule */].forChild(__WEBPACK_IMPORTED_MODULE_2__appliances__["a" /* AppliancesPage */]),
            ],
        })
    ], AppliancesPageModule);
    return AppliancesPageModule;
}());

//# sourceMappingURL=appliances.module.js.map

/***/ }),

/***/ 595:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return AppliancesPage; });
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
 * Generated class for the AppliancesPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */
var AppliancesPage = (function () {
    //appliances;
    function AppliancesPage(navCtrl, navParams, ApiProvider) {
        this.navCtrl = navCtrl;
        this.navParams = navParams;
        this.ApiProvider = ApiProvider;
        this.page = 1;
        this.perPage = 0;
        this.totalData = 0;
        this.totalPage = 0;
    }
    AppliancesPage.prototype.ionViewDidLoad = function () {
        var _this = this;
        console.log('ionViewDidLoad AppliancesPage');
        this.ApiProvider.getAppliances().subscribe(function (res) {
            console.log(res);
            _this.appliances = res;
        });
        console.log(this.appliances);
    };
    AppliancesPage.prototype.navigateToApplianceDetailsPage = function (appliance) {
        console.log(appliance);
        console.log('Navigating to appliance details page.');
        this.navCtrl.push('ApplianceDetailsPage', { 'appliance': appliance });
    };
    AppliancesPage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-appliances',template:/*ion-inline-start:"C:\Users\Roderick\Documents\HomeSimulator\mobile-app\homesimulator\src\pages\appliances\appliances.html"*/'<ion-header>\n\n\n\n  <ion-navbar>\n\n    <ion-title>Appliances</ion-title>\n\n  </ion-navbar>\n\n\n\n</ion-header>\n\n\n\n\n\n<ion-content class="background" padding>\n\n\n\n  <ion-card class="rooms-card">\n\n    <ion-scroll scrollY="true">\n\n      <ion-list class="rooms-list">\n\n        <ion-item-group>\n\n          <ion-item-divider class="header-divider" color="light">Appliances</ion-item-divider>\n\n          <ion-item text-wrap *ngFor="let appliance of appliances" class="room-item" (click)="navigateToApplianceDetailsPage(appliance)">\n\n            <ion-label>Appliance Name: {{appliance.appliancename}}, SensorID: {{appliance.sensorid}}, Power Usage: {{appliance.powerusage}}</ion-label>\n\n          </ion-item>\n\n        </ion-item-group>\n\n      </ion-list>\n\n    </ion-scroll>\n\n  </ion-card>\n\n\n\n</ion-content>\n\n'/*ion-inline-end:"C:\Users\Roderick\Documents\HomeSimulator\mobile-app\homesimulator\src\pages\appliances\appliances.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["e" /* NavController */], __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["f" /* NavParams */], __WEBPACK_IMPORTED_MODULE_2__providers_api_api__["a" /* ApiProvider */]])
    ], AppliancesPage);
    return AppliancesPage;
}());

//# sourceMappingURL=appliances.js.map

/***/ })

});
//# sourceMappingURL=8.js.map