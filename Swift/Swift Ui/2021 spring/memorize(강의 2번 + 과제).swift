//
//  ContentView.swift
//  Memorize
//
//  Created by 정종헌 on 2021/11/29.
//

import SwiftUI

struct ContentView: View {
    var Vehicle = ["✈️", "🚙", "🏎", "🚊" , "🚘" , "🚖" , "🚈", "⛵️", "🚀", "🚡", "🛺", "🚓", "🚌", "🚑", "🚒","🗼"]
    var People = ["👶", "👧", "🧒", "👦", "👩", "🧑", "👨", "👩‍🦱", "🧑🏻‍🦰", "👨🏻‍🦰" , "👱🏻‍♀️", "👱🏻" , "👱🏻‍♂️", "👩🏻‍🦳", "🧑🏻‍🦳","👨🏻‍🦳"]
    var Smaili = ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣" , "🥲", "☺️", "😊", "😇" , "🙂", "🙃", "😉", "😌"]
    @State var emojiCount = 16
    
    @State var emojis = ["✈️", "🚙", "🏎", "🚊" , "🚘" , "🚖" , "🚈", "⛵️", "🚀", "🚡", "🛺", "🚓", "🚌", "🚑", "🚒","🗼"]
    
    var body: some View {
        //이 변수는 함수임. 그래서 리턴값이 있어야하는데 리턴 해주는 항목이 안보임. ㄴㄴ 있음
        VStack{
            Text("Memorize!").font(.title)
            ScrollView{
                LazyVGrid(columns: [GridItem(.adaptive(minimum: 65))]){
                    ForEach(emojis[0..<emojiCount], id : \.self , content:{ emoji in
                        CardView(content: emoji).aspectRatio(2/3, contentMode: .fit)
                    })
                }
            }.foregroundColor(/*@START_MENU_TOKEN@*/.red/*@END_MENU_TOKEN@*/)
            Spacer()
            HStack{
                VButton
                Spacer()
                PButton
                Spacer()
                SButton
            }
            .font(.largeTitle)
            .padding(.horizontal)
            .foregroundColor(.blue)
        }
        .padding(.horizontal)
    }
    
    
    var VButton : some View{
        Button{
            emojis.removeAll()
            emojis = Vehicle
            emojis.shuffle()
        } label:{
            VStack{
                Image(systemName: "car")
                Text("차량").font(.body)
            }
        }
    }
    
    var PButton : some View{
        Button{
            emojis.removeAll()
            emojis = People
            emojis.shuffle()
        } label:{
            VStack{
                Image(systemName: "person")
                Text("사람").font(.body)
            }
        }
    }
    
    var SButton : some View{
        Button{
            emojis.removeAll()
            emojis = Smaili
            emojis.shuffle()
        } label:{
            VStack{
                Image(systemName: "face.smiling")
                Text("스마일리").font(.body)
            }
        }
    }
}


struct CardView: View{
    var content : String
    @State var isFaceUp : Bool = true

    var body: some View{
        ZStack {
            let shape = RoundedRectangle(cornerRadius: 20)
            if isFaceUp {
                // 사각형 생성
                shape.fill().foregroundColor(.white)
                shape.strokeBorder(lineWidth: 3)
                // 텍스트 생성
                Text(content).font(.title).foregroundColor(Color.red)
            }else {
                    shape.fill()
            }
        }
        .onTapGesture {
            isFaceUp = !isFaceUp
        }
    }
}















//프리뷰와 관련된 코드여서 건들일 별로없음
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .preferredColorScheme(.dark)
        ContentView()
            .preferredColorScheme(.light)
    }
}



//
//var emojis = ["✈️", "🚙", "🏎", "🚊" , "🚘" , "🚖" , "🚈", "⛵️", "🚀", "🚡", "🛺", "🚓", "🚌", "🚑", "🚒","🗼"]
//@State var emojiCount = 16
//
//var body: some View {
//    //이 변수는 함수임. 그래서 리턴값이 있어야하는데 리턴 해주는 항목이 안보임. ㄴㄴ 있음
//    VStack{
//        Text("Memorize!")
//        ScrollView{
//            LazyVGrid(columns: [GridItem(.adaptive(minimum: 65))]){
//                ForEach(emojis[0..<emojiCount], id : \.self , content:{ emoji in
//                    CardView(content: emoji).aspectRatio(2/3, contentMode: .fit)
//                })
//            }
//        }.foregroundColor(/*@START_MENU_TOKEN@*/.red/*@END_MENU_TOKEN@*/)
//        Spacer()
//        HStack{
//            remove
//            Spacer() // 오브젝트 사이에 공간을 만들어주는 객체
//            add
//        }
//        .font(.largeTitle)
//        .padding(.horizontal)
//        .foregroundColor(.blue)
//    }
//    .padding(.horizontal)
//}
//
//var remove : some View{
//    Button {
//        if emojiCount > 0{
//            emojiCount -= 1
//        }
//    } label: {
//        Image(systemName: "minus.circle")
//    }
//}
//var add : some View{
//    Button {
//        if emojiCount < emojis.count{
//            emojiCount += 1
//        }
//    } label: {
//        Image(systemName: "plus.circle")
//    }
//}
//}
//
//
//struct CardView: View{
//var content : String
//@State var isFaceUp : Bool = false
//
//var body: some View{
//    ZStack {
//        let shape = RoundedRectangle(cornerRadius: 20)
//        if isFaceUp {
//            // 사각형 생성
//            shape.fill().foregroundColor(.white)
//            shape.strokeBorder(lineWidth: 3)
//            // 텍스트 생성
//            Text(content).font(.title).foregroundColor(Color.red)
//        }else {
//                shape.fill()
//        }
//    }
//    .onTapGesture {
//        isFaceUp = !isFaceUp
//    }
//}
