//
//  EmojiMemoryGame.swift
//  Memorize
//
//  Created by 정종헌 on 2021/12/08.
//

// ViewModel

import SwiftUI


// 클래스 안의 모든 데이터는 꼭 초기화가 되어있어야함.
class EmojiMemoryGame : ObservableObject{
    
    // static 전역변수이긴 하나 클래스안에 소속되어있음..?  3
    static let emojis = ["✈️", "🚙", "🏎", "🚊" , "🚘" , "🚖" , "🚈", "⛵️", "🚀", "🚡", "🛺", "🚓", "🚌", "🚑", "🚒","🗼"]

    static func createMemoryGame() -> MemoryGame<String>{
        MemoryGame<String>(numberOfPairsOfCards: 3)  { pairIndex in emojis[pairIndex]}
        // init 이 되지 않은상황에 안에있는 속성을 사용하는것은 불가능.  1
        // 전역변수로 되어있는 변수는 가져올수있음.  2
    }
    //마찬가지로 전역변수로 쓸수있으나 어디에서 사용하는 함수인지 구분하기위해 클래스안에 넣어두고 사용
        
    @Published private var model : MemoryGame<String> = createMemoryGame()
    //@Published 모델에서 바뀌는값을 뷰모델이 계속보면서 변화하는것을 감지..?
    // 한개의 변수나 함수만 뷰모델이 확인하기를 원하면     objectWillChange.send() 를 확인시키고싶은 곳에 작성하면됨.
     
    var cards: Array<MemoryGame<String>.Card>{
        model.cards
    }
    
    // MARK: - Intent(s)
    func choose(_ card: MemoryGame<String>.Card){
        model.choose(card)
    }
}
