// "switch"문을 사용해 작성된 아래 코드를 if..else문을 사용한 코드로 변환해 보세요.

switch (browser) {
  case 'Edge':
    alert( "Edge를 사용하고 계시네요!" );
    break;

  case 'Chrome':
  case 'Firefox':
  case 'Safari':
  case 'Opera':
    alert( '저희 서비스가 지원하는 브라우저를 사용하고 계시네요.' );
    break;

  default:
    alert( '현재 페이지가 괜찮아 보이길 바랍니다!' );
}

if(browser == 'Edge') alert( "Edge를 사용하고 계시네요!" );
else if(browser == 'Chrome' || browser ==  'Firefox' ||browser ==  'Safari' ||browser ==  'Opera') alert( '저희 서비스가 지원하는 브라우저를 사용하고 계시네요.' )
else alert( '현재 페이지가 괜찮아 보이길 바랍니다!' );

// 아래 코드를 switch문을 사용한 코드로 바꿔보세요. switch문은 하나만 사용해야 합니다.

let a = +prompt('a?', '');

if (a == 0) {
  alert( 0 );
}
if (a == 1) {
  alert( 1 );
}

if (a == 2 || a == 3) {
  alert( '2,3' );
}


switch(a){
    case a == 0:
        alert(0);
        break;
    case a == 1:
        alert(1);
        break;
    case a == 2 || a == 3:
        alert('2,3');
        break;
}

// case a == 2 || a == 3:
//     alert('2,3');
//     break;

// 위 케이스는

// case 2:
// case 3:
//     alert('2,3');
//     break;

// 으로 한번에 묶을수 있음.