import {
  Component,
  ViewChild
} from '@angular/core';
import {
  IonicPage,
  NavController,
  NavParams
} from 'ionic-angular';
import {
  ApiProvider
} from '../../providers/api/api';
import * as Chart from 'chartjs';


/**
 * Generated class for the PowervisualizationPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-powervisualization',
  templateUrl: 'powervisualization.html',
})
export class PowerVisualizationPage {

  @ViewChild('barCanvas')barCanvas;

  weekdata: object;
  monthdata: object;
  barChart: any;



  constructor(public navCtrl: NavController, public navParams: NavParams, public ApiProvider: ApiProvider) {
    this.ApiProvider.getWeekofUsage().subscribe(res => {
      console.log(res);
      this.weekdata = res;
    })
    this.ApiProvider.getMonthofUsage().subscribe(res => {
      console.log(res);
      this.monthdata = res;
    })
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad PowervisualizationPage');

    this.barChart = new Chart(this.barCanvas.nativeElement, {
 
      type: 'bar',
      data: {
          labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
          datasets: [{
              label: '# of Votes',
              data: [12, 19, 3, 5, 2, 3],
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 159, 64, 0.2)'
              ],
              borderColor: [
                  'rgba(255,99,132,1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(255, 159, 64, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          scales: {
              yAxes: [{
                  ticks: {
                      beginAtZero:true
                  }
              }]
          }
      }

  });
  }

  ionViewDidEnter() {

  }

}
