//
//  MemoryGame.swift
//  Memorize
//
//  Created by 정종헌 on 2021/12/08.
//

// model
import Foundation

struct MemoryGame<CardContent> where CardContent : Equatable{
    private(set) var cards : Array<Card>
    
    private var indexOfTheOneOnlyFaceUp : Int?
    //원래는 초기화가 안되어있어서 실행이 안되어야하지만 ?(optional)을 붙여줌으로써 예외처리시킴
    
    //mutating : self를 바꾸는것은 기본적으로 안되게 되어있음 mutating 키워드를 함수앞에 붙여줌으로써 바꿀수있게 설정함
    mutating func choose(_ card: Card){
        // if 조건문 사용시 상수가 들어올경우 &&는 사용불가능 ,으로 대체 가능
        if let chosenIndex = cards.firstIndex(where: {$0.id == card.id }),
            !cards[chosenIndex].isFaceUp,
            !cards[chosenIndex].isMatched {
            if let potentialMatchIndex = indexOfTheOneOnlyFaceUp{
                //cards[i].content 들끼리 비교가 불가능하나 구조체 전체에 위에 where로 선언해준것처럼 선언해주면 비교 가능
                if cards[chosenIndex].content  == cards[potentialMatchIndex].content{
                    cards[chosenIndex].isMatched = true
                    cards[potentialMatchIndex].isMatched = true
                }
                indexOfTheOneOnlyFaceUp = nil
            }else{
                //0..<cards.count == cards.indices
                for i in cards.indices{
                    cards[i].isFaceUp = false
                }
                indexOfTheOneOnlyFaceUp = chosenIndex
            }
            cards[chosenIndex].isFaceUp.toggle()
            // 기본적으로 let으로 되어있음.
            // 이렇게 여기서 변수를 바꾼다고 해도 ui가 자동으로 변경되지는 않음.
        }
        print("\(cards)")
    }

    // 아래 코드와 위코드는 같은 작업을 수행함
    // if let chosenIndex = index(of:card) {
    //             cards[chosenIndex].isFaceUp.toggle()
    //}
    // of (외적인 이름) card (내적인 이름)
//    func index(of card: Card) -> Int? {
//        for i in 0..<cards.count{
//            if cards[i].id == card.id{
//                return i
//            }
//        }
//        return nil //bogus
//    }
    
    //초기화
    init(numberOfPairsOfCards : Int, createCardContent : (Int)-> CardContent){
        cards = Array<Card>()
        // add numberOfPairsOfCards x 2 Cards to cards array
        for pairIndex in 0..<numberOfPairsOfCards {
            let content = createCardContent(pairIndex)
            cards.append(Card(content: content, id: pairIndex*2))
            cards.append(Card(content: content, id: pairIndex*2+1))
        }
        
    }
    
    //Identifiable?
    struct Card: Identifiable {
        var isFaceUp : Bool = false
        var isMatched : Bool = false
        //미리 구조체에 기본값을 부여해주면 구조체를 다른곳에서 생성시 생략가능
        var content : CardContent
        
        var id: Int

    }
}
