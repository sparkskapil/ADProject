map2 = function(){
    var date = new Date(0);
    date.setUTCSeconds(this.Timestamp);
    var key = date.getFullYear()+"-"+month;
    var value = this.Price;
    emit(key,value);
}

map3 = function(){
    var date = new Date(0);
    date.setUTCSeconds(this.Timestamp);
    month =  date.getMonth();
    month = ("0" + month).slice(-2);
    var key = date.getFullYear()+"-"+month;
    var value = this.Price;
    emit(key,value);
}

reduce2 = function(key,values){
	var ucount = 0;
	var dcount = 0;
	var usum=0;
	var dsum=0;
    var result={"AverageIncrease":0,"AverageDecrease":0,"UpsCount":0,"DownsCount":0};
	for(var i=0;i<values.length-1;i++){
		var diff = values[i+1] - values[i];

		if(diff > 0)
		{
			ucount++;
			usum+=diff;
		}
		if(diff < 0){
			diff*=-1;
			dcount++;
			dsum+=diff;
		}
	}
	result.AverageIncrease = usum/ucount;
	result.AverageDecrease = dsum/dcount;
	result.UpsCount = ucount;
	result.DownsCount = dcount;
	return result;
}

db.BitfinexUSD.mapReduce(map2,reduce2,{out:"TrendsYearly"})
db.BitfinexUSD.mapReduce(map3,reduce2,{out:"TrendsMonthly"})

