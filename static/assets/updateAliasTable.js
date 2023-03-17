function updateAliasTable() {
    $.ajax({
      url: "/alias_list_json",
      dataType: "json",
      success: function(data) {
        var tableBody = $("#alias-table tbody");
        tableBody.empty();
        $.each(data, function(i, alias) {
          var row = "<tr><td>" + alias.name + "</td><td>" + alias.ip_address + "</td><td>" + alias.description + "</td></tr>";
          tableBody.append(row);
        });
      },
      error: function() {
        alert("Problème !!!!!!!!!!!!!!!!");
      }
    });
  }

  $(document).ready(function() {
    updateAliasTable();
    setInterval(updateAliasTable, 5000);
  });
  
  