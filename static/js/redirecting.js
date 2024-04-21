$(document).ready(function() {
    $('.nav-link').click(function(event) {
        event.preventDefault();
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
        event.preventDefault();
        var redirectUrl = $(this).attr('href');
        window.location.href = redirectUrl;        
    });

    $('.card-link').click(function(event) {
        event.preventDefault();
        var source = $(this).data('source');
        $.ajax({
            url: '/process_data',
            method: 'POST',
            data: {source: source},
            success: function(response) {
                window.location.href = response;
            },
            error: function(xhr, status, error) {
                console.error("Error making POST request:", error);
            }
        });
    });

    $('.dropdown-item').click(function(event) {
        event.preventDefault();
        var source = $(this).data('source');
        $.ajax({
            url: '/update_record',
            method: 'POST',
            data: {source: source},
            success: function(response) {
                window.location.href = response;
            },
            error: function(xhr, status, error) {
                console.error("Error making POST request:", error);
            }
        });
    });

});