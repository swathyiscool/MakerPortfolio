
import SwiftUI

@main
struct carecompanionappApp: App {
    
    let persistenceController = PersistenceController.shared
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
            //FamilyContacts()
                //.environment(\.managedObjectContext, ContactsProvider.shared.viewContext)
            
        }
    }
}
