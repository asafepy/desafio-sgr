(function($) {
    
    function resetOption(mensagem){
        $('#id_prgrama')
            .find('option')
            .remove()
            .end()
            .append('<option value="">'+mensagem+'</option>')
            .val('');
    }
    function resetOption2(){
        $('#id_prgrama')
            .find('option')
            .remove();
    }

    function getProgramas(radio){

        $.get({
            type: "GET",
            url: "/api/programa/",
            dataType: "json",
            data:{'radio':radio},
            success: function (data) {
                
                resetOption2();

                let htmlOption;
                $.each(data, function(key, val){
                    $("#id_prgrama option[value='"+val.id+"']").remove();
                    htmlOption += "<option value='"+val.id+"'>"+val.nome+"</option>";
                });
                $("#id_prgrama").append(htmlOption);

            }
        });
    }

    $(document).ready(function() {
        
        url = window.location.href; 
        if( url.indexOf("change") == -1){
            resetOption("Selecione uma rádio");
        }
        

        $('#id_radio').on('change', function() {
            getProgramas(this.value);
        });

        // $('#id_programa').on('change', function() {
        //     alert(this.value);
        // });
    });

})(django.jQuery);