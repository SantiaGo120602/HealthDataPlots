$(document).ready(function() {
    // Target all elements with the class 'nav-link'
    $('.nav-link').click(function(event) {
        event.preventDefault(); // Prevent default behavior of anchor tag
        // Get the URL from the href attribute of the clicked element
        var redirectUrl = $(this).attr('href');
        if (redirectUrl === "/reporte"){
            if (window.location.pathname === '/plotting'){
                console.log("Implementar reporte");
            }
            else {
                console.log("Página incorrecta");
            }
        }
        else{
            window.location.href = redirectUrl;
        }
    });

    $('principal-page-button').click(function(event) {
        event.preventDefault(); // Prevent default behavior of anchor tag
        // Get the URL from the href attribute of the clicked element
        var redirectUrl = $(this).attr('href');
        window.location.href = redirectUrl;        
    });
});