import { Component, ViewChild } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { Chart } from 'chart.js';
import { ApiProvider } from '../../providers/api/api';
var _ = require('lodash');

@IonicPage()
@Component({
  selector: 'page-powervisualization',
  templateUrl: 'powervisualization.html',
})
export class PowerVisualizationPage {
  @ViewChild('monthlyLineCanvas') monthlyLineCanvas;
  @ViewChild('dailyLineCanvas') dailyLineCanvas;

  monthlyLineChart: any;
  monthlyData;
  monthlyDates;
  monthlyPowerCost;
  monthlyTotalPowerUsage;
  monthlyTotalHvacCost;
  monthlyTotalHvacUseage;
  monthlyTotalWaterCost;
  monthlyTotalWaterUseage;

  dailyLineChart: any;
  dailyData;
  dailyDates;
  dailyPowerCost;
  dailyTotalPowerUsage;
  dailyTotalHvacCost;
  dailyTotalHvacUseage;
  dailyTotalWaterCost;
  dailyTotalWaterUseage;

  constructor(public navCtrl: NavController, public navParams: NavParams, public ApiProvider: ApiProvider) {
  }

  CreateDailyChart(){
    this.dailyLineChart = new Chart(this.dailyLineCanvas.nativeElement, {
            type: 'line',
            data: {
                labels: this.dailyDates,
                datasets: [{
                       data: this.dailyPowerCost,
                       label: "Total Power Cost",
                       borderColor: "#3e95cd",
                       fill: false
                     }, {
                       data: this.dailyTotalHvacCost,
                       label: "Total HVAC Cost",
                       borderColor: "#8e5ea2",
                       fill: false
                     }, {
                       data: this.dailyTotalWaterCost,
                       label: "Total Water Cost",
                       borderColor: "#3cba9f",
                       fill: false
                     }, {
                       data: this.dailyTotalPowerUsage,
                       label: "Total Power Useage",
                       borderColor: "#e8c3b9",
                       fill: false
                     }, {
                       data: this.dailyTotalHvacUseage,
                       label: "Total Hvac Useage",
                       borderColor: "#c45850",
                       fill: false
                     }, {
                       data: this.dailyTotalWaterUseage,
                       label: "Total Water Useage",
                       borderColor: "#c45454",
                       fill: false
                     }

                   ]
            },
            options: {
              title: {
                    display: true,
                    text: 'Daily Data'
                  }
            }

        });
  }

  CreateMonthlyChart(){
    this.monthlyLineChart = new Chart(this.monthlyLineCanvas.nativeElement, {
            type: 'line',
            data: {
                labels: this.monthlyDates,
                datasets: [{
                       data: this.monthlyPowerCost,
                       label: "Total Power Cost",
                       borderColor: "#3e95cd",
                       fill: false
                     }, {
                       data: this.monthlyTotalHvacCost,
                       label: "Total HVAC Cost",
                       borderColor: "#8e5ea2",
                       fill: false
                     }, {
                       data: this.monthlyTotalWaterCost,
                       label: "Total Water Cost",
                       borderColor: "#3cba9f",
                       fill: false
                     }, {
                       data: this.monthlyTotalPowerUsage,
                       label: "Total Power Useage",
                       borderColor: "#e8c3b9",
                       fill: false
                     }, {
                       data: this.monthlyTotalHvacUseage,
                       label: "Total Hvac Useage",
                       borderColor: "#c45850",
                       fill: false
                     }, {
                       data: this.monthlyTotalWaterUseage,
                       label: "Total Water Useage",
                       borderColor: "#c45454",
                       fill: false
                     }

                   ]
            },
            options: {
              title: {
                    display: true,
                    text: 'Monthly Data'
                  }
            }

        });

  }


  ionViewDidLoad() {
    console.log('load');
    this.ApiProvider.getMonthofUsage().subscribe(res => {
      console.log(res)
      this.dailyData = res
      this.dailyDates = _.map(this.dailyData, 'date');
      this.dailyTotalHvacCost = _.map(this.dailyData, 'totalhvaccost');
      this.dailyTotalHvacUseage = _.map(this.dailyData,'totalhvacusage');
      this.dailyPowerCost = _.map(this.dailyData,'totalpowercost');
      this.dailyTotalPowerUsage = _.map(this.dailyData,'totalpowerusage');
      this.dailyTotalWaterCost = _.map(this.dailyData,'totalwatercost');
      this.dailyTotalWaterUseage = _.map(this.dailyData,'totalwaterusage');
      this.CreateDailyChart();
    });

    this.ApiProvider.getWeekofUsage().subscribe(res => {
      console.log(res)
      this.monthlyData = res
      this.monthlyDates = _.map(this.monthlyData, 'date');
      this.monthlyTotalHvacCost = _.map(this.monthlyData, 'totalhvaccost');
      this.monthlyTotalHvacUseage = _.map(this.monthlyData,'totalhvacusage');
      this.monthlyPowerCost = _.map(this.monthlyData,'totalpowercost');
      this.monthlyTotalPowerUsage = _.map(this.monthlyData,'totalpowerusage');
      this.monthlyTotalWaterCost = _.map(this.monthlyData,'totalwatercost');
      this.monthlyTotalWaterUseage = _.map(this.monthlyData,'totalwaterusage');
      this.CreateMonthlyChart();
    })
  }

}
