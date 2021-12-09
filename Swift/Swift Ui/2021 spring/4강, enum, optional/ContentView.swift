//
//  ContentView.swift
//  Memorize
//
//  Created by 정종헌 on 2021/11/29.
//

//View

import SwiftUI

struct ContentView: View {
    @ObservedObject var viewModel : EmojiMemoryGame
    
    var body: some View {
        //이 변수는 함수임. 그래서 리턴값이 있어야하는데 리턴 해주는 항목이 안보임. ㄴㄴ 있음
        ScrollView{ 
                LazyVGrid(columns: [GridItem(.adaptive(minimum: 65))]){
                    ForEach(viewModel.cards) { card in
                        CardView(card: card)
                            .aspectRatio(2/3, contentMode: .fit)
                            .onTapGesture {
                                viewModel.choose(card)
                            }
                    }
                }
            }
            .foregroundColor(/*@START_MENU_TOKEN@*/.red/*@END_MENU_TOKEN@*/)
            .padding(.horizontal)
    }

    

struct CardView: View{
    let card : MemoryGame<String>.Card
    // 읽기전용 변수다보니 굳이 var로 할필요가없음
    
    var body: some View{
        ZStack {
            let shape = RoundedRectangle(cornerRadius: 20)
            if card.isFaceUp {
                // 사각형 생성
                shape.fill().foregroundColor(.white)
                shape.strokeBorder(lineWidth: 3)
                // 텍스트 생성
                Text(card.content).font(.title).foregroundColor(Color.red)
            }else if card.isMatched {
                shape.opacity(0.0)
//                카드가 일치하게 됬다면 카드의 투명도를 0으로
            }
            else {
                    shape.fill()
            }
        }
    }

    }
}






//프리뷰와 관련된 코드여서 건들일 별로없음
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        let game = EmojiMemoryGame()
        ContentView(viewModel: game)
            .preferredColorScheme(.dark)
        ContentView(viewModel: game)
            .preferredColorScheme(.light)
    }
}


