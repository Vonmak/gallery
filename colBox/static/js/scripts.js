function copyToClipBoard() {
    var copyText = document.getElementById("myInput");

    copyText.select();
    copyText.setSelectionRange(0, 99999);

    document.execCommand("copy");
    alert("Copied!");
}

$(function() {
    $('button[data-toggle="tooltip"]').tooltip({
        animated: "fade",
        placement: "top",
        trigger: "click",
    });
});