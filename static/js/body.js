
$('.body_buttons_span').click(function(){
    var isotope = $('.isotope')
    isotope.css('display', 'none');
    $('.body_buttons_span').css({
        "background-color":'white'
        
    })
    $('.body_buttons_span').children().css({
        'color': "#2e3131",
        
    })
    $(this).css({
        "background-color": "#ef3e42",
        "color": "white"
    })

    

    for (var i=0; i<isotope.length; i++){
        if ($(this).data('type') ==  $(isotope[i]).data('type')){
            
            $(isotope[i]).css('display', 'block');
            
        }
    }
})

$('.menu-dropdown  .menu-dropdown-arrow').on('click', function(){
    $('#menu-list').addClass('active')
    $(this).closest('.menu-dropdown').addClass('active')
})
$('.menu-dropdown .menu-dropdown-goback').on('click', function(){
    $('#menu-list').removeClass('active');
    $(this).closest('.menu-dropdown').removeClass('active');
})


document.querySelector('.btn-burger').addEventListener('click', function(){
var header = document.querySelector('.header-none')

header.classList.add('d-none')
document.querySelector('.menu').classList.add('d-block')

})

document.querySelector('.menu-close-btn').addEventListener('click', function(){
var header = document.querySelector('.header-none')
var menu = document.querySelector('.menu')
header.classList.remove('d-none')
menu.classList.remove('d-block')
})

document.querySelector('.search-bar button').addEventListener('click', function(e){
e.stopPropagation();
this.parentNode.classList.toggle('active');

});

document.addEventListener("click", function(elem){
const element = elem.target;
if(element.id != "search-input"){
    document.querySelector('.search-bar').classList.remove('active')
}
})



