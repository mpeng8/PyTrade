
function predictStockJS(){
  $.ajax({
    type:"GET",
    url:"/predictStocks",
    success: function(result) {
      result = result.data;
      //console.log(result);
      document.getElementById("defaultPredictDiv").innerHTML = "You should " +result + " tomorrow";
    },
    fail: function() {
      alert('Woops, we are unable to predict your stock');
    }
  });

}
