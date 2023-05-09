let doc = document;
if (doc.querySelector('.btnDel1')) {
  let btnDel1 = doc.querySelectorAll('.btnDel1');
  for (let i = 0; i < btnDel1.length; i++) {
    btnDel1[i].addEventListener('click', function(event) {
      if (confirm('Deseja mesmo apagar este dado?')) {
        return true;
      } else {
        event.preventDefault();
      }
    });
  }
}