document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('modal');
    var modalImg = document.getElementById("modal-image");
    var modalCaption = document.getElementById("modal-caption");
    var images = document.querySelectorAll('.gallery img');
    var closeBtn = document.getElementsByClassName("close")[0];

    images.forEach(image => {
        image.addEventListener('click', function() {
            modal.style.display = "block";
            modalImg.src = this.src;
            modalCaption.innerHTML = this.nextElementSibling.innerHTML;
            modalCaption.style.bottom = "10px";
        });
    });

    closeBtn.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});
