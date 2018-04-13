webpackJsonp([6],{

/***/ 288:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "RoomsPageModule", function() { return RoomsPageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__rooms__ = __webpack_require__(879);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



var RoomsPageModule = (function () {
    function RoomsPageModule() {
    }
    RoomsPageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["I" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_2__rooms__["a" /* RoomsPage */],
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["d" /* IonicPageModule */].forChild(__WEBPACK_IMPORTED_MODULE_2__rooms__["a" /* RoomsPage */]),
            ],
        })
    ], RoomsPageModule);
    return RoomsPageModule;
}());

//# sourceMappingURL=rooms.module.js.map

/***/ }),

/***/ 879:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return RoomsPage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__providers_api_api__ = __webpack_require__(105);
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
 * Generated class for the RoomsPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */
var RoomsPage = (function () {
    function RoomsPage(navCtrl, navParams, ApiProvider) {
        this.navCtrl = navCtrl;
        this.navParams = navParams;
        this.ApiProvider = ApiProvider;
    }
    RoomsPage.prototype.ionViewDidLoad = function () {
        var _this = this;
        console.log('ionViewDidLoad RoomsPage');
        this.ApiProvider.getRooms().subscribe(function (res) {
            console.log(res);
            _this.rooms = res;
        });
    };
    RoomsPage.prototype.navigateToRoomPage = function (room) {
        console.log(room);
        console.log('Navigating to room details page.');
        this.navCtrl.push('RoomPage', { 'room': room });
    };
    RoomsPage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-rooms',template:/*ion-inline-start:"C:\Users\Roderick\Documents\HomeSimulator\mobile-app\homesimulator\src\pages\rooms\rooms.html"*/'<ion-header>\n\n\n\n  <ion-navbar>\n\n    <ion-title>Rooms</ion-title>\n\n  </ion-navbar>\n\n\n\n</ion-header>\n\n\n\n\n\n<ion-content class="background" padding>\n\n\n\n  <ion-card class="rooms-card">\n\n    <ion-scroll scrollY="true">\n\n      <ion-list class="rooms-list">\n\n        <ion-item-group>\n\n          <ion-item-divider class="header-divider" color="light">Rooms</ion-item-divider>\n\n          <ion-item *ngFor="let room of rooms" class="room-item" (click)="navigateToRoomPage(room)">\n\n            {{room.roomname}}\n\n          </ion-item>\n\n        </ion-item-group>\n\n      </ion-list>\n\n    </ion-scroll>\n\n  </ion-card>\n\n\n\n</ion-content>\n\n'/*ion-inline-end:"C:\Users\Roderick\Documents\HomeSimulator\mobile-app\homesimulator\src\pages\rooms\rooms.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["e" /* NavController */], __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["f" /* NavParams */], __WEBPACK_IMPORTED_MODULE_2__providers_api_api__["a" /* ApiProvider */]])
    ], RoomsPage);
    return RoomsPage;
}());

//# sourceMappingURL=rooms.js.map

/***/ })

});
//# sourceMappingURL=6.js.map