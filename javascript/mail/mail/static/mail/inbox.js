document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#ViewEmail-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
  
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#ViewEmail-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  
  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3 id="mailbox_h">${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  load(mailbox);
}

function ViewEmail (id){
  // Show the mail and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#ViewEmail-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  document.querySelector("#ViewEmail-view").innerHTML = "";

  var requestOptions = {
    method: 'GET'
  };

  fetch(`/emails/${id}`, requestOptions)
  .then(response => response.json())
  .then(result => {
      
      let div = document.createElement("div");

      
      let sender = document.createElement("h3");
      sender.innerHTML = result.sender;
      div.appendChild(sender);

      let recipients = document.createElement("h6");
      recipients.innerHTML = `To: ${result.recipients}`;
      div.appendChild(recipients);
      
      let subject = document.createElement("h5");
      subject.innerHTML = result.subject;
      div.appendChild(subject);
      
      let timestamp = document.createElement("p");
      timestamp.innerHTML = result.timestamp;
      div.appendChild(timestamp);

      let body = document.createElement("p");
      body.innerHTML = result.body;
      div.appendChild(body);
      
      let mailbox = document.querySelector('#mailbox_h').innerHTML;
      if (mailbox != 'Sent') {
        let archived = document.createElement("button");
        archived.onclick = () => archive_mail(id, result.archived)
        archived.innerHTML = result.archived?'unarchive': 'archive';
        div.appendChild(archived);

        let reply = document.createElement("button");
        reply.onclick = () => reply_mail(result.sender, result.subject, result.body, result.timestamp)
        reply.innerHTML = 'Reply';
        div.appendChild(reply);


      }

      document.querySelector('#ViewEmail-view').appendChild(div);
    }
  )
  .catch(error => console.log('error', error))

  var requestOptions = {
    method: 'PUT',
    body: JSON.stringify({
      read: true
  })
  };

  fetch(`/emails/${id}`, requestOptions)
  .then(response => console.log(response))
  
}

function reply_mail(sender, subject, body, timestamp) {
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#ViewEmail-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  document.querySelector('#compose-recipients').value = sender;
  document.querySelector('#compose-subject').value = `Re: ${subject}`;
  document.querySelector('#compose-body').value = `On ${timestamp} ${sender} wrote: \n ${body}`;
}

function archive_mail(id, boolean) {
  var requestOptions = {
    method: 'PUT',
    body: JSON.stringify({
      archived: !boolean
  })
  };

  fetch(`/emails/${id}`, requestOptions)
  .then(response => console.log(response),
    load_mailbox('inbox'))
  
}


function load(mailbox) {

  var requestOptions = {
    method: 'GET'
  };
  
  fetch(`/emails/${mailbox}`, requestOptions)
  .then(response => response.json())
  .then(result => {
    for (let i = 0; i < result.length; i++) {
      let sender = result[i].sender;
      let subject = result[i].subject;
      let timestamp = result[i].timestamp;
      
      let div = document.createElement("div");
      div.onclick = () => ViewEmail(result[i].id);
      div.className = "mail_div";

      div.style.backgroundColor = result[i].read? "#AAA": "#FFF";
      
      let h3 = document.createElement("h3");
      h3.innerHTML = sender;
      div.appendChild(h3);
      
      let h5 = document.createElement("h5");
      h5.innerHTML = subject;
      div.appendChild(h5);
      
      let p = document.createElement("p");
      p.innerHTML = timestamp;
      div.appendChild(p);

      let input = document.createElement("input");

      document.querySelector('#emails-view').appendChild(div);
    }
  })
  .catch(error => console.log('error', error))
}

function send() {
  
  let recipients = document.querySelector('#compose-recipients').value;
  let subject = document.querySelector('#compose-subject').value;
  let body = document.querySelector('#compose-body').value;

  var requestOptions = {
    method: 'POST',
    body: JSON.stringify({
      recipients: recipients,
      subject: subject,
      body: body
    })
  };
  
  fetch('/emails', requestOptions)
  .then(response => response.json())
  .then(result => { console.log(result)})
  .catch(error => console.log('error', error))

  load_mailbox('sent');
  return false;
}