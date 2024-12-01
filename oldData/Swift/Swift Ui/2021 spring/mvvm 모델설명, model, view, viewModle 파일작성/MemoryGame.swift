//
//  MemoryGame.swift
//  Memorize
//
//  Created by 정종헌 on 2021/12/08.
//

// model
import Foundation

struct MemoryGame<CardContent>{
    private(set) var cards : Array<Card>
    
    func choose(_ card: Card){
        
    }
    
    //초기화
    init(numberOfPairsOfCards : Int, createCardContent : (Int)-> CardContent){
        cards = Array<Card>()
        // add numberOfPairsOfCards x 2 Cards to cards array
        for pairIndex in 0..<numberOfPairsOfCards {
            let content = createCardContent(pairIndex)
            cards.append(Card(content: content))
            cards.append(Card(content: content))
        }
        
    }
    
    struct Card{
        var isFaceUp : Bool = false
        var isMatched : Bool = false
        //미리 구조체에 기본값을 부여해주면 구조체를 다른곳에서 생성시 생략가능
        var content : CardContent
    }
}
