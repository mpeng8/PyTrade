var sss = [["fuck", "you"], ["fuck", "school"], ["fuck", "life"]];
function predictStockJS(){
  $.ajax({
    type:"GET",
    url:"/predictStocks",
    success: function(result) {
        // console.log(result);
        // console.log(typeof result);
        // console.log(typeof sss);

        if (document.getElementById("defaultPredictDiv") != null) {
          var result = result.data;
          document.getElementById("defaultPredictDiv").innerHTML = "You should " +result + " tomorrow";
        } else {
          var jsarray = JSON.parse(result);
          // console.log(aaa);
          // console.log(typeof aaa);
          $("#example").dataTable({
              retrieve: true,
              data: jsarray,
              columns: [
              { title: "Date" },
              { title: "Suggestion" },
              ]
          });
        };

      },
    fail: function() {
      alert('Woops, we are unable to predict your stock');
    }
  });

}
