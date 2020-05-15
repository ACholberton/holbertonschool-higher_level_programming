// Javascript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML’s tag DIV#hello //
$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: function (data) {
    $('DIV#hello').text(data.hello);
  }
});
