import { Component, ViewChild  } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { Chart } from 'chart.js';
import { ApiProvider } from '../../providers/api/api';
var _ = require('lodash');
var moment = require('moment');

@IonicPage()
@Component({
  selector: 'page-watervisualization',
  templateUrl: 'watervisualization.html',
})
export class WaterVisualizationPage {
  @ViewChild('monthlyLineCanvas') monthlyLineCanvas;
  @ViewChild('dailyLineCanvas') dailyLineCanvas;

  monthlyLineChart: any;
  monthlyData;
  monthlyDates;
  monthlyTotalWaterCost;
  monthlyTotalWaterUsage;

  dailyLineChart: any;
  dailyData;
  dailyDates;
  dailyTotalWaterCost;
  dailyTotalWaterUsage;

  constructor(public navCtrl: NavController, public navParams: NavParams, public ApiProvider: ApiProvider) {
  }


  CreateDailyChart(){
    this.dailyLineChart = new Chart(this.dailyLineCanvas.nativeElement, {
            type: 'line',
            data: {
                labels: this.dailyDates,
                datasets: [{
                       data: this.dailyTotalWaterCost,
                       label: "Total Water Cost",
                       borderColor: "#3e95cd",
                       fill: false
                     },{
                       data: this.dailyTotalWaterUsage,
                       label: "Total Water Useage",
                       borderColor: "#e8c3b9",
                       fill: false
                     }
                   ]
            },
            options: {
              options: {
              scales: {
                  xAxes: [{
                      type: 'time',
                      time: {
                          displayFormats: {
                              quarter: 'MMM YYYY'
                          }
                      }
                  }]
              }
          }
            }

        });
  }

  CreateMonthlyChart(){
    console.log(this.dailyDates);
    this.monthlyLineChart = new Chart(this.monthlyLineCanvas.nativeElement, {
            type: 'line',
            data: {
                labels: this.monthlyDates,
                datasets: [{
                       data: this.monthlyTotalWaterCost,
                       label: "Total Water Cost",
                       borderColor: "#3e95cd",
                       fill: false
                     }, {
                       data: this.monthlyTotalWaterUsage,
                       label: "Total Water Useage",
                       borderColor: "#e8c3b9",
                       fill: false
                     }
                   ]
            },
            options: {
              title: {
                    display: true,
                    text: 'Monthly Water Data'
                  }
            }
        });

  }



  ionViewDidLoad() {
    console.log('ionViewDidLoad WatervisualizationPage');
    this.ApiProvider.getMonthofUsage().subscribe(res => {
      console.log(res)
      this.dailyData = res
      var t = _.map(this.dailyData, 'date');
      this.dailyDates = t.map(function(v) {
        return moment(v).format('MMM DD');
      });
      this.dailyTotalWaterCost = _.map(this.dailyData,'totalwatercost');
      this.dailyTotalWaterUsage = _.map(this.dailyData,'totalwaterusage');
      console.log(this.dailyTotalWaterUsage)
      this.CreateDailyChart();
    });

    this.ApiProvider.getWeekofUsage().subscribe(res => {
      console.log(res)
      this.monthlyData = res
      var q = _.map(this.monthlyData, 'date');
      this.monthlyDates = q.map(function(v) {
        return moment(v).format('MMM DD');
      });
      this.monthlyTotalWaterCost = _.map(this.monthlyData,'totalwatercost');
      this.monthlyTotalWaterUsage = _.map(this.monthlyData,'totalwaterusage');
      this.CreateMonthlyChart();
    });

  }

}
