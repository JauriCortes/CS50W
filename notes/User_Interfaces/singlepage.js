// Show one page and hides the other two
function showSection(section) {

    fetch(`/sections/${section}`)
    .then(response => response.text())
    .then(text => {
        console.log(text);
        document.querySelector('#content').innerHTML = text;
    })
}

//Wait for page to loaded
document.addEventListener('DOMContentLoaded', function() {

    // Select all buttons
    document.querySelectorAll("button").forEach(button => {

        //When a button is clicked, switch to that page
        button.onclick = function() {
            showSection(this.dataset.page);
        }
    })

})