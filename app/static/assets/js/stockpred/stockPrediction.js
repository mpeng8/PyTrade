
function predictStockJS(){
  $.ajax({
    type:"GET",
    url:"/predictStocks",
    success: function(result) {
      result = result.data;
      document.getElementById("defaultPredictDiv").innerHTML = "You should " +result + " tomorrow";
        $("#example").dataTable({
            data: result
        });
      }

    },
    fail: function() {
      alert('Woops, we are unable to predict your stock');
    }
  });

}
