(function($) {
    
    function resetOption(mensagem){
        $('.field-programa > div > select')
            .find('option')
            .remove()
            .end()
            .append('<option value="">'+mensagem+'</option>')
            .val('');
    }
    function resetOption2(){
        $('.field-programa > div > select')
            .find('option')
            .remove();
    }

    function getProgramas(radio){
        alert("entrou");
        $.get({
            type: "GET",
            url: "/api/programa/",
            dataType: "json",
            data:{'radio':radio},
            success: function (data) {
                
                resetOption2();

                let htmlOption;
                $.each(data, function(key, val){
                    $(".field-programa > div > select option[value='"+val.id+"']").remove();
                    htmlOption += "<option value='"+val.id+"'>"+val.nome+"</option>";
                });
                $(".field-programa > div > select").append(htmlOption);

            }
        });
    }

    $(document).ready(function() {
        
        url = window.location.href; 
        if( url.indexOf("change") != -1){
            
        }
        

        $('#id_radio').on('change', function() {
            getProgramas(this.value);
        });

        $('.field-programa > div > select').on('change', function() {
            alert(this.value);
        });
    });

})(django.jQuery);