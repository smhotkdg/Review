function searchToggle(obj, evt){
    var container = $(obj).closest('.search-wrapper');
        if(!container.hasClass('active')){
            container.addClass('active');
            //evt.preventDefault();            
        }
        else if(container.hasClass('active') && $(obj).closest('.input-holder').length == 0){
            container.removeClass('active');
            // clear input
            container.find('.search-input').val('');
        }        
        else
        {
            
        }
}

window.onload = function() { // window.addEventListener('load', (event) => {와 동일합니다.
    
    searchToggle($("#btn1"))
};
