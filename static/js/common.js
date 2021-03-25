// // // ここにコードを書いていく
// // console.log("Javascriptが読み込まれていれば表示されます");
// //
// // var sunabako = "スナバコ";
// // // console.log(sunabako);
// //
// // sunabako = "沖縄県沖縄市中央1-14-3";
// // console.log(sunabako);
// //
// //
// // console.log(1+2);
// // console.log(3-1);
// // console.log(2*3);
// // console.log(3/2);
// // console.log(5%3);
// //
// // console.log("ここから下がaの計算結果になります");
// // console.log("----------------------------");
// // var a = 0;
// //
// // console.log(a);
// //
// // a = 1;
// //
// // console.log(a);
// //
// // // 2 = 1 + 1;
// // // もしくは
// // a += 1;
// //
// // console.log(a);
// //
// // a -= 1;
// //
// // // 1 = 2 - 1 ;
// //
// // console.log(a);
// //
// //
// // console.log("ここから下がbの計算結果になります");
// // console.log("----------------------------");
// //
// //
// //
// // var b = 1;
// //
// // console.log(b);
// //
// // console.log(++b);
// // // b = b + 1;
// //
// // console.log(b++);
// // console.log(b);
// //
// //
// // console.log(--b);
// // // b = b - 1;
// //
// // console.log(b--);
// // console.log(b);
// //
// // console.log("suna" + "bako");
// //
// // var c = "suna" ;
// // var d = "bako" ;
// //
// // console.log(c + d);
// //
// // console.log("ここから下が文字列の分割の結果になります");
// // console.log("----------------------------");
// //
// //
// // console.log("su:na:ba:ko".split(":"));
// //
// //
// //
// // console.log("ここから下が真偽値のコンソール結果になります");
// // console.log("----------------------------");
// //
// //
// // var e = 2 ;
// // var f = 2 ;
// //
// // console.log(e == f);
// // console.log(e != f);
// // console.log(e > f);
// // console.log(e >= f);
// // console.log(e < f);
// // console.log(e <= f);
// //
// //
// //
// // console.log("ここからの++gの結果になります");
// // console.log("----------------------------");
// //
// // var g = 1 ;
// //
// // console.log(g);
// //
// // console.log(g++);   //g = 2
// // console.log(g++);
// // console.log(g++);
// // console.log(g++);
// // console.log(g++);
// // console.log(g++);
// // console.log(g++);
// // console.log(g++);
// // console.log(g++);
// // console.log(g++);
// // console.log(g++);
// // console.log(g++);
// //
// //
// //
// // console.log("ここからの配列のお話になります");
// // console.log("----------------------------");
// //
// //
// // var h = [5 , 10 , 15];
// // console.log(h[1]);
// //
// // console.log(h[2]);
// //
// // h[2] = 50 ;
// // console.log(h[2]);
// //
// //
// //
// // console.log("ここからのオブジェクト、連想配列のお話になります");
// // console.log("----------------------------");
// //
// // var book = { タイトル: "sunabakoの始まり" , total_page : 200, author : "スナバコ" };
// //
// // console.log(book["タイトル"]);
// // book["total_page"] = 100 ;
// // console.log(book["total_page"]);
//
//
// var a = 3;
// var b = 2;
//
// if( a < b ){
//
// console.log(" aはbより小さい ");
//
// } else if ( a == b ) {
//
//   console.log("a,bは等しい");
//
// } else {
//
//   console.log("aはbより大きい");
//
// }
//
//
//
// console.log("ここからの繰り返し文、for文のお話になります");
// console.log("----------------------------");
//
//
//
// var sum = 0 ;
//
// for ( var i = 0 ; i < 10 ; i++ ){
//
//   // sum += i ;
//   // 上の記述は sum = sum + i  と一緒;
//
//   sum += i++ // sum = sum + i
//              // i = i + 1
//   sum += ++i // sum = sum + i(=i+1)
//   if (i<10) {
//
//   }
//
//     console.log(sum);
// }



//
// console.log(text_node.textContent);



// var btn_node = document.getElementById("jsbtn");
// btn_node.addEventListener("mouseup" , changeTxt);
//
// function changeTxt(){
//
//   var text_node = document.getElementById("txt");
//   text_node.textContent = "ノードを更新";
//
// }

// var text_node =document.getElementById("txt");
// text_node.textContent = "ノードを更新";




$(function () {  




$('.dere').on('click',function(){
  var dere_replies = ['やったやん！','すげえ！','最高！','積みあがってるね','ステキやん！','.............','.............','....','で？',
  '.........','褒めてもらうつもり？<br>自分が決めたことをやっただけで？'];
  var dere_repliesNo = Math.floor( Math.random() * dere_replies.length);
    $(".dere_replies").html(dere_replies[dere_repliesNo])
    $(".fukidashi").css("display", "inline-block")
    $(".smile").css("display", "block")
    $(".angry").css("display", "none")
    $(".dere_replies").css("display", "block")
    $(".tun_replies").css("display", "none")
    let row = $(this).closest("tr").fadeOut();
    $(row).fadeOut();

});


$('.tun').on('click',function(){
  var tun_replies = ['駄目やん！','なんでやねん！','がんばれ！','うそつき','理想と現実が離れすぎているのかもね。<br>タスクの中身を細かくしてみたらどう？'
  ,'あなたが今日をどう過ごそうが世界は回るから大丈夫。<br>お前はこれを本当にやりたいの？','...............','たまには出来ない日もあるさ。でも諦めちゃ駄目だよ'
  ,"いい加減出来ない報告は飽きてます","実はこんなタスクリストを見る間に手を付けたほうがよかったりして。。"];
  var tun_repliesNo = Math.floor( Math.random() * tun_replies.length);
  $(".tun_replies").html(tun_replies[tun_repliesNo])
  $(".fukidashi").css("display", "inline-block")
  $(".smile").css("display", "none")
  $(".angry").css("display", "block")
  $(".tun_replies").css("display", "block")
  $(".dere_replies").css("display", "none")
});


// 通知の許可と表示の設定
window.onload = function() {
  Notification.requestPermission();
  // 時間になったら関数notificationを実行
  setInterval(notification, 5000);   
};

let previousMinutes;

const notification = function() {
  // 現在の時刻を取得
   const date = new Date();
  //  inputタグで入力された時間を取得
   var notifi_time = document.getElementById( "time" ).value ;
   if (previousMinutes !== notifi_time && minutes % 15 === 0) {
       previousMinutes = minutes;
      //  ダブルクォーテーションの中が表示される文字
       const notification = new Notification("Check!");
   }
};




});