//
//  ContactDetailView.swift
//  CCapp
//
//  Created by Saraswathy Amjith on 8/28/23.
//

import SwiftUI

struct TaskDetailView: View {
    let dailytask: DailyTask
    
    var body: some View {
        List {
            Section("General") {
                
                LabeledContent {
                    Text(dailytask.taskname)
                } label: {
                    Text("To Do")
                }
                
            }
            Section ("Notes") {
                Text(dailytask.notes)
            }
        }
        .navigationTitle(dailytask.taskname)
    }
}

/* struct ContactDetailView_Previews: PreviewProvider {
    static var previews: some View {
        NavigationStack {
            ContactDetailView()
        }
    }
}
*/
