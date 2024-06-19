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

function toggleUploadOption(radio, childId) {
    var fileUpload = document.getElementById("file-upload-" + childId);
    var urlUpload = document.getElementById("url-upload-" + childId);

    if (radio.value === "file") {
        fileUpload.style.display = "block";
        urlUpload.style.display = "none";
        document.querySelector(`#file-upload-${childId} input`).required = true;
        document.querySelector(`#url-upload-${childId} input`).required = false;
    } else if (radio.value === "url") {
        fileUpload.style.display = "none";
        urlUpload.style.display = "block";
        document.querySelector(`#file-upload-${childId} input`).required = false;
        document.querySelector(`#url-upload-${childId} input`).required = true;
    }
}
