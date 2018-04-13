webpackJsonp([4],{

/***/ 291:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "TemperaturePageModule", function() { return TemperaturePageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__temperature__ = __webpack_require__(881);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



var TemperaturePageModule = (function () {
    function TemperaturePageModule() {
    }
    TemperaturePageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["I" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_2__temperature__["a" /* TemperaturePage */],
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["d" /* IonicPageModule */].forChild(__WEBPACK_IMPORTED_MODULE_2__temperature__["a" /* TemperaturePage */]),
            ],
        })
    ], TemperaturePageModule);
    return TemperaturePageModule;
}());

//# sourceMappingURL=temperature.module.js.map

/***/ }),

/***/ 881:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return TemperaturePage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(28);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var TemperaturePage = (function () {
    function TemperaturePage(navCtrl, navParams) {
        this.navCtrl = navCtrl;
        this.navParams = navParams;
        this.temperature = 50;
    }
    TemperaturePage.prototype.ionViewDidLoad = function () {
        console.log('ionViewDidLoad TemperaturePage');
        //var slider = (document.getElementById("myslider") as HTMLInputElement);
        //var output = (document.getElementById("output"));
        //output.innerHTML = slider.value; // Display the default slider value
        //slider.oninput = function() {
        //output.innerHTML = (this as HTMLInputElement).value;
    };
    TemperaturePage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-temperature',template:/*ion-inline-start:"C:\Users\Roderick\Documents\HomeSimulator\mobile-app\homesimulator\src\pages\temperature\temperature.html"*/'<ion-header>\n\n\n\n  <ion-navbar>\n\n    <ion-title>Temperature</ion-title>\n\n  </ion-navbar>\n\n\n\n</ion-header>\n\n\n\n\n\n<ion-content class="background" padding>\n\n\n\n\n\n  <ion-card class="temperature-card">\n\n    <!--<ion-item-divider class="header-divider" color="light">Temperature</ion-item-divider> -->\n\n    <ion-card-header text-wrap>\n\n      <p id="temp-title"> <b> Current House Temperature</b> </p>\n\n    </ion-card-header>\n\n    <h3 id="output">{{temperature}}\n\n      <span id="degrees"></span>\n\n    </h3>\n\n    <!--<div class="slidecontainer">\n\n      <input type="range" min="1" max="100" value="50" class="slider" id="myslider">\n\n    </div> -->\n\n    <ion-item >\n\n      <ion-range id="temprange" min="50" max="100" step="1" snaps="true" color="danger" [(ngModel)]="temperature"></ion-range>\n\n      <!--<ion-label range-left>50</ion-label>\n\n      <ion-label range-left>100</ion-label> -->\n\n    </ion-item>\n\n\n\n  </ion-card>\n\n\n\n</ion-content>\n\n'/*ion-inline-end:"C:\Users\Roderick\Documents\HomeSimulator\mobile-app\homesimulator\src\pages\temperature\temperature.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["e" /* NavController */], __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["f" /* NavParams */]])
    ], TemperaturePage);
    return TemperaturePage;
}());

//# sourceMappingURL=temperature.js.map

/***/ })

});
//# sourceMappingURL=4.js.map