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
    var fileInput = document.getElementById("id_file_name");
    var urlInput = document.getElementById("id_url");

    if (radio.value === "file") {
        fileUpload.style.display = "block";
        fileInput.required = true;
        urlUpload.style.display = "none";
        urlInput.required = false;
    } else {
        fileUpload.style.display = "none";
        fileInput.required = false;
        urlUpload.style.display = "block";
        urlInput.required = true;
    }
}
