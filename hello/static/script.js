
// Kakao MAP
/*var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
var options = { //지도를 생성할 때 필요한 기본 옵션
	center: new kakao.maps.LatLng(33.450701, 126.570667), //지도의 중심좌표.
	level: 3 //지도의 레벨(확대, 축소 정도)
};

var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴*/


// Polynominal
var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(35.88390603320519,  128.5961273987009), // 지도의 중심좌표
        level: 2 // 지도의 확대 레벨
    };

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

// 다각형을 구성하는 좌표 배열입니다. 이 좌표들을 이어서 다각형을 표시합니다
var polygonPath = [
        new kakao.maps.LatLng(35.88441721228444, 128.59597432494832),
        new kakao.maps.LatLng(35.88425396617738, 128.59571359175698),
        new kakao.maps.LatLng(35.884042443222114, 128.59654262035588),
        new kakao.maps.LatLng(35.884251652541025, 128.5967350685148),
        new kakao.maps.LatLng(35.88440994056632, 128.59601293607082),
];

// 지도에 표시할 다각형을 생성합니다
var polygon = new kakao.maps.Polygon({
    path:polygonPath, // 그려질 다각형의 좌표 배열입니다
    strokeWeight: 3, // 선의 두께입니다
    strokeColor: '#39DE2A', // 선의 색깔입니다
    strokeOpacity: 0.8, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
    strokeStyle: 'solid', // 선의 스타일입니다
    fillColor: '#A2FF99', // 채우기 색깔입니다
    fillOpacity: 0.7 // 채우기 불투명도 입니다
});

// 지도에 다각형을 표시합니다
polygon.setMap(map);

// 다각형에 마우스오버 이벤트가 발생했을 때 변경할 채우기 옵션입니다
var mouseoverOption = {
    fillColor: '#EFFFED', // 채우기 색깔입니다
    fillOpacity: 0.8 // 채우기 불투명도 입니다
};

// 다각형에 마우스아웃 이벤트가 발생했을 때 변경할 채우기 옵션입니다
var mouseoutOption = {
    fillColor: '#A2FF99', // 채우기 색깔입니다
    fillOpacity: 0.7 // 채우기 불투명도 입니다
};

// 다각형에 마우스오버 이벤트를 등록합니다
kakao.maps.event.addListener(polygon, 'mouseover', function() {

    // 다각형의 채우기 옵션을 변경합니다
    polygon.setOptions(mouseoverOption);

});

kakao.maps.event.addListener(polygon, 'mouseout', function() {

    // 다각형의 채우기 옵션을 변경합니다
    polygon.setOptions(mouseoutOption);

});

// 다각형에 마우스다운 이벤트를 등록합니다
var downCount = 0;
kakao.maps.event.addListener(polygon, 'mousedown', function() {
    console.log(event);
    var resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '삼성 창조 캠퍼스 주차장' + (++downCount);
});
