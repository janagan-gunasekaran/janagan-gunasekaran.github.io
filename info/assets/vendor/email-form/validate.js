/**
* PHP Email Form Validation - v3.5
* URL: https://bootstrapmade.com/php-email-form/
* Author: BootstrapMade.com
*/
(function () {
  "use strict";

  let forms = document.querySelectorAll('.php-email-form');

  forms.forEach( function(e) {
    e.addEventListener('submit', function(event) {
      event.preventDefault();

      let thisForm = this;
      thisForm.querySelector('.loading').classList.add('d-block');
      thisForm.querySelector('.error-message').classList.remove('d-block');
      thisForm.querySelector('.sent-message').classList.remove('d-block');

      email_form_submit(thisForm);

    });
  });

  function email_form_submit(thisForm) {
    var params = {
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      message: document.getElementById("message").value
    };
  
    const serviceID = "service_p601fv9";
    const templateID = "template_fo79xvi";
  
      emailjs.init("jW_9pGQpRlHNOTDOl");
      emailjs.send(serviceID, templateID, params)
      .then(res=>{
          document.getElementById("name").value = "";
          document.getElementById("email").value = "";
          document.getElementById("message").value = "";
          console.log(res);
          thisForm.querySelector('.loading').classList.remove('d-block');
          thisForm.querySelector('.sent-message').classList.add('d-block');
      })
      .catch(err=>{
        console.log(err);
        displayError(thisForm, err);
      });    
  }

  function displayError(thisForm, error) {
    thisForm.querySelector('.loading').classList.remove('d-block');
    thisForm.querySelector('.error-message').innerHTML = error;
    thisForm.querySelector('.error-message').classList.add('d-block');
  }

})();
