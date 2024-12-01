//
//  MemorizeApp.swift
//  Memorize
//
//  Created by 정종헌 on 2021/11/29.
//

import SwiftUI

@main
struct MemorizeApp: App {
    let game = EmojiMemoryGame()
    var body: some Scene {
        WindowGroup {
            ContentView(viewModel: game)
        }
    }
}
