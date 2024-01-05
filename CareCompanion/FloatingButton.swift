//
//  FloatingButton.swift
//  carecompanionapp
//
//  Created by Saraswathy Amjith on 7/26/23.
//

import SwiftUI

struct FloatingButton: View {
    var body: some View {
                Spacer()
                HStack {
                    NavigationLink(destination: ContentView()) {
                        Text("+ New Task")
                            .font(.headline)
                    }
                    .padding(15)
                    
                    .foregroundColor(.white)
                    
                    .background(Color.accentColor)
                    
                    .cornerRadius(38)
                    
                    .padding(3)
                    
                    .shadow(color: .black.opacity(0.3), radius: 3, x: 3, y: 3)
                }
            }
        }
    

struct FloatingButton_Previews: PreviewProvider {
    static var previews: some View {
        FloatingButton()
    }
}
