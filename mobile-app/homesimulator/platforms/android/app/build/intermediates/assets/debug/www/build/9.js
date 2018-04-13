webpackJsonp([9],{

/***/ 282:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppliancedetailsPageModule", function() { return AppliancedetailsPageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__appliancedetails__ = __webpack_require__(594);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



var AppliancedetailsPageModule = (function () {
    function AppliancedetailsPageModule() {
    }
    AppliancedetailsPageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["I" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_2__appliancedetails__["a" /* ApplianceDetailsPage */],
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["d" /* IonicPageModule */].forChild(__WEBPACK_IMPORTED_MODULE_2__appliancedetails__["a" /* ApplianceDetailsPage */]),
            ],
        })
    ], AppliancedetailsPageModule);
    return AppliancedetailsPageModule;
}());

//# sourceMappingURL=appliancedetails.module.js.map

/***/ }),

/***/ 594:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return ApplianceDetailsPage; });
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
 * Generated class for the AppliancedetailsPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */
var ApplianceDetailsPage = (function () {
    function ApplianceDetailsPage(navCtrl, navParams, ApiProvider) {
        this.navCtrl = navCtrl;
        this.navParams = navParams;
        this.ApiProvider = ApiProvider;
        this.onoffswitch = false;
        this.result = { 'sensorname': 'guestbathroomlightsensor', 'sensorid': 8, 'applianceid': 23, 'appliancename': 'guestbathroomlight', 'poweruseage': 12, 'powerrate': 1.14, 'status': 0 };
        console.log(this.navParams);
        this.appliance = this.navParams.data.appliance;
        console.log(this.appliance);
        this.id = this.appliance.applianceid;
        this.name = this.appliance.appliancename;
        this.powerrate = this.appliance.powerrate;
        this.powerusage = this.appliance.powerusage;
    }
    ApplianceDetailsPage.prototype.ionViewDidLoad = function () {
        console.log('ionViewDidLoad AppliancedetailsPage');
        console.log(this.name);
        console.log(this.id);
    };
    ApplianceDetailsPage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-appliancedetails',template:/*ion-inline-start:"C:\Users\Roderick\Documents\HomeSimulator\mobile-app\homesimulator\src\pages\appliancedetails\appliancedetails.html"*/'<!--\n\n  Generated template for the AppliancedetailsPage page.\n\n\n\n  See http://ionicframework.com/docs/components/#navigation for more info on\n\n  Ionic pages and navigation.\n\n-->\n\n<ion-header>\n\n\n\n  <ion-navbar>\n\n    <ion-title>{{name}} Details</ion-title>\n\n  </ion-navbar>\n\n\n\n</ion-header>\n\n\n\n\n\n<ion-content class="background" padding>\n\n\n\n  <ion-card class="detailscard">\n\n    <ion-item-divider class="header-divider" color="light">{{name}} Details</ion-item-divider>\n\n\n\n    <div class=text-container text-center>\n\n      <ion-label color="dark2" >On/Off Switch</ion-label>\n\n      <ion-toggle text-center id="onoffswitch" [(ngModel)]="onoffswitch"></ion-toggle>\n\n      <p *ngIf="onoffswitch" class="powerstatus">The {{name}} is on</p>\n\n      <p>The powerrate is: {{powerrate}} cents per watt.</p>\n\n      <p>The {{name}} has used {{powerusage}} watts of power.</p>\n\n    </div>\n\n\n\n  </ion-card>\n\n\n\n\n\n</ion-content>\n\n'/*ion-inline-end:"C:\Users\Roderick\Documents\HomeSimulator\mobile-app\homesimulator\src\pages\appliancedetails\appliancedetails.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["e" /* NavController */], __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["f" /* NavParams */], __WEBPACK_IMPORTED_MODULE_2__providers_api_api__["a" /* ApiProvider */]])
    ], ApplianceDetailsPage);
    return ApplianceDetailsPage;
}());

//# sourceMappingURL=appliancedetails.js.map

/***/ })

});
//# sourceMappingURL=9.js.map