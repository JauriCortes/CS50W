if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0)
}

let count =() => {

    let counter = localStorage.getItem('counter');

    counter++
    document.querySelector('h1').innerHTML = counter;

    localStorage.setItem('counter', counter)
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    
    setInterval(count, 1000);
})