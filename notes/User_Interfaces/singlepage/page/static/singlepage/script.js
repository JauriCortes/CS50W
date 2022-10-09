//start with first post
let counter = 1;

//load posts 20 at a time
const quantity = 20;

// when DOM loads, render the first 20 posts
document.addEventListener('DOMContentLoaded', load);

//If scrolled to bottom, load the next 20 posts
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

function load() {
    // Set start and end post numbers, and update counter
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;

    //Get new posts and add posts
    fetch(`/posts?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        data.posts.forEach(add_post);
    })

    // Add a new post with given contents to DOM
    function add_post(contents) {

        //create new post
        const post = document.createElement('div');
        post.className = 'post';
        post.innerHTML = contents;

        // Add post to DOM
        document.querySelector('#posts').append(post);
    }
}
