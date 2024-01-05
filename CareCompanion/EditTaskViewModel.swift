//
//  EditContactViewFile.swift
//  CCapp
//
//  Created by Saraswathy Amjith on 8/28/23.
//

import Foundation
import CoreData

final class EditTaskViewModel: ObservableObject {
    
    @Published var dailytask: DailyTask
    
    private let context: NSManagedObjectContext
    
    init(provider: TasksProvider, dailytask: DailyTask? = nil) {
        self.context = provider.newContext
        self.dailytask = DailyTask(context: self.context)
        
    }
    
    func save() throws {
        if context.hasChanges {
            try context.save()
        }
    }
}
