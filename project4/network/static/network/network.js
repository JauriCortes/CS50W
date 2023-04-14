document.addEventListener('DOMContentLoaded', function() {

    // hide all textareas
    document.querySelectorAll(".editarea").forEach((editarea) => {
        
        editarea.style.display = 'none';
        textarea = editarea.querySelector('textarea');


        //textarea.value = ""
         
        })


    //hide post when edit button is clicked
    document.querySelectorAll(".edit").forEach((button) => {
        button.addEventListener('click', (e) => {

            const parent = e.target.parentNode;
            parent.style.display = 'none';

            id = parent.id.replace("post_", "")
            content = document.getElementById(`content_${id}`)
            
            editarea = document.getElementById(`editarea_${id}`)

            textarea = editarea.querySelector('textarea')
            textarea.value = content.innerHTML

            editarea.style.display = 'block';
        })
    })
    
    //go look for the submit button
    document.querySelectorAll(".submit").forEach((button) => {
        button.addEventListener('click', (e) => {
            
            const parent = e.target.parentNode;
            
            parent.style.display = 'none';

            textarea = parent.querySelector('textarea');
            id = parent.id.replace("editarea_", "")

            content = document.getElementById(`content_${id}`)
            content.innerHTML = textarea.value
            
            post = document.getElementById(`post_${id}`)
            post.style.display = 'block';
        })
    })
})
