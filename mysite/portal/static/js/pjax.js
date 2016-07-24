function pjax () {

  $.pjax({
    area : '.js-pjax',
    link : '.js-submit',
    load: {
      head: 'base, meta, link',
      css: true,
      script: true
    },
    ajax: { timeout: 3000 }, 
    wait : 700,
    // scrollTop: false
  });

  
  $(document)
    .on('pjax:fetch', function() {
      $('body').animate({opacity:0}, 500);
    })
    .on('pjax:DOMContentLoaded', function(){
      $('body').css({opacity:0});
    })
    .on('pjax:render', function() {
      $('body').animate({opacity:1}, 200);
    });
}
