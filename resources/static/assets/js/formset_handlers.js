(function($) {
    
    function resetOption(mensagem){
        $('.field-programa > div > select')
            .find('option')
            .remove()
            .end()
            .append('<option value="">'+mensagem+'</option>')
            .val('');
    }


    function getProgramas(radio){
        $.get({
            type: "GET",
            url: "/api/radio/"+radio+"/",
            dataType: "json",
            success: function (data) {
                
                resetOption("Selecione um programa...");

                let htmlOption;
                $.each(data['programas'], function(key, val){
                    $(".field-programa > div > select > option[value='"+val.id+"']").remove();
                    htmlOption += "<option value='"+val.id+"'>"+val.nome+"</option>";
                });
                $(".field-programa > div > select").append(htmlOption);

            }
        });
    }

    $(document).ready(function() {
        
        url = window.location.href; 
        if( url.indexOf("change") != -1){
            resetOption("Selecione uma rádio...");    
        }
        
        

        $('#id_radio').on('change', function() {
            getProgramas(this.value);
        });

        // $('.field-programa > div > select').on('change', function() {
        //     alert(this.value);
        // });
    });

})(django.jQuery);