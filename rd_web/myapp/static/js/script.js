document.addEventListener("DOMContentLoaded", function () {
    var openModalButtons = document.querySelectorAll(".open-modal");
    var closeModalButtons = document.querySelectorAll(".close");

    openModalButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var childId = button.getAttribute("data-child-id");
            var modal = document.getElementById("modal-" + childId);
            modal.style.display = "block";
        });
    });

    closeModalButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var childId = button.getAttribute("data-child-id");
            var modal = document.getElementById("modal-" + childId);
            modal.style.display = "none";
        });
    });

    window.addEventListener("click", function (event) {
        closeModalButtons.forEach(function (button) {
            var childId = button.getAttribute("data-child-id");
            var modal = document.getElementById("modal-" + childId);
            if (event.target == modal) {
                modal.style.display = "none";
            }
        });
    });
});
