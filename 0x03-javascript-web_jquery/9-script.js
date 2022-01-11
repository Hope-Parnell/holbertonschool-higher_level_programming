$(document).ready(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data, status) => {
    if (status === 'success') {
      $('DIV#hello').text(data.hello);
    }
  });
});
