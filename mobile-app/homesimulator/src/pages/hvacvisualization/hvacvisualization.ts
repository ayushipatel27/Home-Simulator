import { Component, ViewChild } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { Chart } from 'chart.js';
import { ApiProvider } from '../../providers/api/api';
// var _ = require('lodash');
// var moment = require('moment');
import * as _ from "lodash";
import * as moment from 'moment';

@IonicPage()
@Component({
  selector: 'page-hvacvisualization',
  templateUrl: 'hvacvisualization.html',
})
export class HvacvisualizationPage {

  @ViewChild('monthlyLineCanvas') monthlyLineCanvas;
  @ViewChild('dailyLineCanvas') dailyLineCanvas;

  monthlyLineChart: any;
  monthlyData;
  monthlyDates;
  monthlyHVACCost;
  monthlyTotalHVACUsage;

  dailyLineChart: any;
  dailyData;
  dailyDates;
  dailyHVACCost;
  dailyTotalHVACUsage;

  constructor(public navCtrl: NavController, public navParams: NavParams, public ApiProvider: ApiProvider) {
  }

  CreateDailyChart(){
    this.dailyLineChart = new Chart(this.dailyLineCanvas.nativeElement, {
            type: 'line',
            data: {
                labels: this.dailyDates,
                datasets: [{
                       data: this.dailyHVACCost,
                       label: "Total HVAC Cost",
                       borderColor: "#3e95cd",
                       fill: false
                     },{
                       data: this.dailyTotalHVACUsage,
                       label: "Total HVAC Useage",
                       borderColor: "#e8c3b9",
                       fill: false
                     }
                   ]
            },
            options: {
              title: {
                    display: true,
                    text: 'Daily HVAC Data'
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
                       data: this.monthlyHVACCost,
                       label: "Total HVAC Cost",
                       borderColor: "#3e95cd",
                       fill: false
                     }, {
                       data: this.monthlyTotalHVACUsage,
                       label: "Total HVAC Useage",
                       borderColor: "#e8c3b9",
                       fill: false
                     }
                   ]
            },
            options: {
              title: {
                    display: true,
                    text: 'Monthly Power Data'
                  }
            }
        });
  }


  ionViewDidLoad() {
    console.log('load');

    this.ApiProvider.getWeekofUsage().subscribe(res => {
      console.log(res)
      this.dailyData = res
      var t = _.map(this.dailyData, 'date');
      this.dailyDates = t.map(function(v) {
        return moment(v).format('MMM DD');
      });
      this.dailyHVACCost = _.map(this.dailyData,'totalhvaccost');
      this.dailyTotalHVACUsage = _.map(this.dailyData,'totalhvacusage');

      this.CreateDailyChart();
    });

    this.ApiProvider.getMonthofUsage().subscribe(res => {
      console.log(res)
      this.monthlyData = res
      this.monthlyDates = _.map(this.monthlyData, 'date');
      var q = _.map(this.monthlyData, 'date');
      this.monthlyDates = q.map(function(v) {
        return moment(v).format('MMM DD');
      });
      this.monthlyHVACCost = _.map(this.monthlyData,'totalhvaccost');
      this.monthlyTotalHVACUsage = _.map(this.monthlyData,'totalhvacusage');
      this.CreateMonthlyChart();
    });
  }

}
