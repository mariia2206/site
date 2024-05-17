    // ваш JavaScript
    document.addEventListener("DOMContentLoaded", function() {
        let slideIndex = 0;
        const prevButton = document.querySelector(".prev");
        const nextButton = document.querySelector(".next");
        const slides = document.querySelectorAll(".testimonial-slide");

        showSlides();

        function plusSlides(n) {
            slideIndex += n;
            showSlides();
        }

        function showSlides() {
            if (slideIndex >= slides.length) {
                slideIndex = 0;
            } else if (slideIndex < 0) {
                slideIndex = slides.length - 1;
            }

            for (let i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }

            slides[slideIndex].style.display = "block";
        }

        prevButton.addEventListener("click", function() {
            plusSlides(-1);
        });

        nextButton.addEventListener("click", function() {
            plusSlides(1);
        });
    });
