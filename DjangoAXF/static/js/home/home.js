$(function () {
    initTopSwiper();
});

function initTopSwiper() {
    var mySwiper = new Swiper ('#topSwiper', {
    direction: 'horizontal',
    loop: true,

    // 如果需要分页器
    pagination: '.swiper-pagination',
  })
}