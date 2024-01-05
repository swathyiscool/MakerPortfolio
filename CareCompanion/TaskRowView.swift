//
//  ContactRowView.swift
//  CCapp
//
//  Created by Saraswathy Amjith on 8/16/23.
//

import SwiftUI

struct TaskRowView: View {
    
    @Environment(\.managedObjectContext) private var moc
    
    @ObservedObject var dailytask: DailyTask
    
    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
           
            Text(dailytask.taskname)
                .font(.callout.bold())
            
            Text(dailytask.notes)
                .font(.callout.bold())
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .overlay(alignment: .topTrailing) {
            Button {
                toggleComplete()
            } label: {
                Image(systemName: "star")
                    .font(.title3)
                    .symbolVariant(.fill)
                    .foregroundColor(dailytask.completed ? .yellow: .gray.opacity(0.3))
            }
            .buttonStyle(.plain)
        }
    }
}

private extension TaskRowView {
    func toggleComplete() {
        dailytask.completed.toggle()
        do {
            if moc.hasChanges {
                try moc.save()
            }
        }catch {
            print(error)
        }
    }
}
//struct ContactRowView_Previews: PreviewProvider {
//    static var previews: some View {
//        ContactRowView()
//    }
//}
