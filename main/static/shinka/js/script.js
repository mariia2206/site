document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('modal');
    var modalImg = document.getElementById("modal-image");
    var modalCaption = document.getElementById("modal-caption");
    var images = document.querySelectorAll('.gallery img');
    var closeBtn = document.getElementsByClassName("close")[0];

    for (var i = 0; i < images.length; i++) {
        images[i].addEventListener('click', function() {
            modal.style.display = "block";
            modalImg.src = this.src;
            modalCaption.innerHTML = this.nextElementSibling.innerHTML;
            // Устанавливаем позицию подписи
            modalCaption.style.bottom = "10px"; // Расположение подписи внизу
            modalCaption.style.left = "50%"; // Положение по центру
            modalCaption.style.transform = "translateX(-50%)"; // Сдвиг по горизонтали влево на 50%
        });
    }

    closeBtn.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});
