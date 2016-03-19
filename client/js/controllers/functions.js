/*
TODO: CORRIGIR TODOS OS CASOS 00
TODO: CORRIGIR ERROR DE POST LOG (ALGUNS NAO APARECEM NO LOG DO HORARIO CERTO)
*/

function getOrganizedScheduleObjects(schedule, logs) {
  var today = new Date("2016-03-08T16:13:00.000Z");
  var newCurrent = [];
  var sched = getClosestSchedules(schedule, today.getHours(), today.getMinutes());

  sched.forEach(function(el, i, a) {
    var temp = {};
    temp["timeScheduled"] = el;
    temp["actualLog"] = [];
    logs.forEach(function(element, index, array) {
      var d = new Date(element.date);
      var predict = predictTime([d.getHours(), d.getMinutes()], element.diff);
      var td = getTimeDifference(predict, el);
       if((el[0] == 13) && (el[1] == 0)) {console.log(el); console.log(predict)};
      if(Math.abs(td)<6) {
        temp["actualLog"].push(element);
      }
    })
    newCurrent.push(temp);
  });
  return newCurrent;
};

function getNumberArrayFromTime(time) {
  time = String(time);
  var s1 = Number(time.substr(0, 2));
  var s2 = Number(time.substr(2, 4));
  return [s1, s2];
}

function getClosestSchedules(sch, h, m) {
  sch.forEach(function(element, index, array) {
    array[index] = getNumberArrayFromTime(element);
  });

  var arrayOfTimes = [];
  var countNext = 0;
  for(var i=0; i<sch.length; i++) {
    if(countNext>0){
     break;
    }
    if(sch[i][0] == h) {
      if(sch[i][1]>m) {
        arrayOfTimes.push(sch[i]);
        countNext++;
      }
    } else if(sch[i][0]>h) {
      arrayOfTimes.push(sch[i]);
      countNext++;
    }
  }

  var countBefore = 0;
  for(var i=(sch.length-1); i>0; i--) {
    if(countBefore>1){
     break;
    }
    if(sch[i][0] == h) {
      if(sch[i][1]<m) {
        arrayOfTimes.push(sch[i]);
        countBefore++;
      }
    } else if(sch[i][0]<h) {
      arrayOfTimes.push(sch[i]);
      countBefore++;
    }
  };

  return arrayOfTimes;
}


function predictTime(time, diff) {
  var hours = time[0];
  var mins = time[1] - diff;
  if(mins<0) {
    hours = hours - 1;
    mins = mins + 60;
    if(hours<0) {
      hours = hours + 24;
    }
  }
  return [hours, mins];
}


function getTimeDifference(t1, t2) {
  if(t1[0] == t2[0]) {
    return Math.abs(t1[1] - t2[1]);
  } else if (t1[0]>t2[0]) {
    return 60*Math.abs(t1[0] - t2[0]) + 60 + t1[1] - t2[1];
  } else if (t1[0]<t2[0]) {
    return 60*Math.abs(t2[0] - t1[0]) + 60 + t2[1] - t1[1];
  }
}

function doubleDigit(number) {
  var s = String(number);
  if(s.length<2) {
    s = "0"+s;
  }
  return s;
}

function getAvgDiff(logs) {
  var diffArray = [];
  logs.forEach(function(el, i, a) {
    diffArray.push(el.diff)
  });
  return getAvg(diffArray);
}

function getAvg(array) {
  var sum = 0;
  for( var i = 0; i < array.length; i++ ){
      sum += parseInt( array[i], 10 ); //don't forget to add the base
  }
  var avg = sum/array.length;
  return avg;
}
