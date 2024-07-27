document.addEventListener("DOMContentLoaded", function() {
  const redHeader = document.querySelector('#red_header');
  const header = document.querySelector('header');
  
  if (redHeader && header) {
      redHeader.addEventListener('click', function() {
          header.style.color = '#FF0000';
      });
  }
});
