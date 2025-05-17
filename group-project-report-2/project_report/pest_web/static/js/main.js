document.addEventListener("DOMContentLoaded", () =>{

    
    const toggelBtn = document.getElementById('big');
    const navLinks = document.getElementById('edit');
    
    toggelBtn.addEventListener('click',()=>{
        navLinks.classList.toggle('show');
});

});

