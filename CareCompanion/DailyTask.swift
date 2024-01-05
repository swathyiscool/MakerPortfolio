//
//  Contact.swift
//  CCapp
//
//  Created by Saraswathy Amjith on 8/16/23.
//

import Foundation
import CoreData

final class DailyTask: NSManagedObject, Identifiable {
    @NSManaged var taskname: String
    @NSManaged var notes: String
    @NSManaged var completed: Bool
    
    
}

extension DailyTask {
    private static var DailyTasksFetchRequest: NSFetchRequest<DailyTask> {
        NSFetchRequest(entityName: "DailyTask")
    }
    
    static func all() -> NSFetchRequest<DailyTask> {
        let request: NSFetchRequest<DailyTask> = DailyTasksFetchRequest
        request.sortDescriptors = [
            NSSortDescriptor(keyPath: \DailyTask.taskname, ascending: true)
            ]
        return request
    }
}
