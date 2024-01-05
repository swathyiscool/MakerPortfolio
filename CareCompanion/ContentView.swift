import SwiftUI
import CoreData
import AVFoundation

struct ContentView: View {
    var body: some View {
        NavigationView {
            ZStack {
                LinearGradient(
                    colors: [Color("mediumblue"), Color("lightblue")],
                    startPoint: .top, endPoint: .bottom)
                .edgesIgnoringSafeArea(.all)
                
                .padding(.leading, 10.0)
                .frame(maxWidth: .infinity, alignment: .leading)
                VStack {
                    Image("bluebear")
                        .imageScale(.large)
                        .foregroundColor(.accentColor)
                    
                    Text("CareCompanion")
                        .font(.title)
                        .fontWeight(.semibold)
                        .foregroundColor(Color("darkblue"))
                    NavigationLink(destination: MenuBar(), label: {Text("Menu")
                        .font(.largeTitle)})
                    
                }
            }
        }
    }
}


struct DailyTasksView: View {
    @State private var tasks: [Task] = [
            Task(title: "eat breakfast", total: 1, completed: 0),
            Task(title: "eat lunch", total: 1, completed: 0),
            Task(title: "eat dinner", total: 1, completed: 0),
            Task(title: "brush teeth", total: 2, completed: 0)
        ]
        @State private var showingAddTask = false

        var body: some View {
            NavigationView {
                List {
                    ForEach(tasks) { task in
                        TaskRow(task: task)
                    }
                    .onDelete(perform: deleteTask)
                }
                .navigationBarTitle("Daily Tasks")
                .navigationBarItems(trailing:
                    Button(action: {
                        showingAddTask.toggle()
                    }) {
                        Image(systemName: "plus")
                    }
                )
                .sheet(isPresented: $showingAddTask) {
                    AddTaskView(tasks: $tasks)
                }
            }
        }

        func deleteTask(at offsets: IndexSet) {
            tasks.remove(atOffsets: offsets)
        }
    }

struct TaskRow: View {
    @State var task: Task
    
    var body: some View {
        HStack {
            Text(task.title)
            Spacer()
            
            Button(action: {
                if task.completed < task.total {
                    task.completed += 1
                } else {
                    task.completed = 0
                }
            }) {
                HStack {
                    Image(systemName: task.completed > 0 ? "checkmark.square" : "square")
                    Text("\(task.completed)/\(task.total) times")
                }
            }
        }
    }
}

struct MenuBar: View {
    var body: some View {
        ZStack {
            LinearGradient(
                colors: [Color("mediumblue"), Color("lightblue")],
                startPoint: .top, endPoint: .bottom)
            .edgesIgnoringSafeArea(.all)
            VStack {
                
                HStack() {
                    
                    Image("bluebear")
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                        .frame(width: 150, height: 150, alignment: .leading)
                    
                    Text("Care Companion")
                        .font(.largeTitle)
                        .fontWeight(.semibold)
                    
                        .frame(maxWidth: .infinity)
                        .foregroundColor(Color("darkblue"))
                    Spacer()
                }
                .edgesIgnoringSafeArea(.all)
                
                // Add some top padding to separate the image and text from the navigation links
                
                NavigationLink(destination: GroceryList(), label: {
                    Text("Grocery List")
                        .font(.title)
                        .fontWeight(.semibold)
                        .foregroundColor(Color("textmenu"))
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color("darkblue"))
                        .cornerRadius(10)
                })
                
                NavigationLink(destination: Mindfullness(), label: {
                    Text("Mindfulness")
                        .font(.title)
                        .fontWeight(.semibold)
                        .foregroundColor(Color("textmenu"))
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color("darkblue"))
                        .cornerRadius(10)
                })
                NavigationLink(destination:    Appointments()
                    .environmentObject(EventStore(preview: true)), label: {
                    Text("Appointments")
                        .font(.title)
                        .fontWeight(.semibold)
                        .foregroundColor(Color("textmenu"))
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color("darkblue"))
                        .cornerRadius(10)
                })
                NavigationLink(destination: DailyTasksView(), label: {
                    Text("Daily Tasks")
                        .font(.title)
                        .fontWeight(.semibold)
                        .foregroundColor(Color("textmenu"))
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color("darkblue"))
                        .cornerRadius(10)
                })
                NavigationLink(destination: FamilyContacts()
                               .environment(\.managedObjectContext, ContactsProvider.shared.viewContext), label: {
                    Text("Family Contacts")
                        .font(.title)
                        .fontWeight(.semibold)
                        .foregroundColor(Color("textmenu"))
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color("darkblue"))
                        .cornerRadius(10)
                })
            }
            
            
        }
    }
}
struct Mindfullness: View {
    
    @StateObject private var vm = ViewModel()

    private let timer = Timer.publish(every: 1, on: .main, in: .common).autoconnect()
    private let buttonSize: CGFloat = 80
    
    var body: some View {
        ZStack {
            LinearGradient(
                colors: [Color("mediumblue"), Color("lightblue")],
                startPoint: .top, endPoint: .bottom)
            .edgesIgnoringSafeArea(.all)
            VStack {
                if vm.isActive {
                    Text("\(vm.time)")
                        .font(.system(size: 70, weight: .medium, design: .rounded))
                        .foregroundColor(Color("darkblue"))
                        .padding()
                        .frame(width: buttonSize * 3, height: buttonSize * 2)
                        .background(.thinMaterial)
                        .cornerRadius(20)
                        .overlay(RoundedRectangle(cornerRadius: 20)
                            .stroke(Color("darkblue"), lineWidth: 4))
                    
                        .alert("Timer done!", isPresented: $vm.showingAlert) {
                            Button("Continue", role: .cancel) {}
                        }
                } else {
                    HStack() {
                        Text("Create a new mediation session ")
                            .font(.system(size: 25, weight: .semibold))
                            .foregroundColor(Color("darkblue"))
                        
                            .frame(maxWidth: 1500)
                        Text("+")
                        
                            .font(.system(size: 70, weight: .semibold))
                            .foregroundColor(Color("darkblue"))
                        
                            .frame(maxWidth: 100)
                            .background(Color("textmenu"))
                    }
                    .background(Color("textmenu"))
                    .cornerRadius(20)
                    .overlay(RoundedRectangle(cornerRadius: 20)
                        .stroke(Color.gray, lineWidth: 2))
                    .padding()
                    
                }
               
                
                Text("select a time")
                    .font(.system(size: 35, weight: .semibold))
                    .foregroundColor(Color("textmenu"))
                    .padding(.horizontal, 40)
                    .background(Color("darkblue"))
                
                
                HStack(spacing: 10) {
                    CircleButton(label: "5", action: { vm.start(minutes: 5) }, isActive: vm.isActive)
                    CircleButton(label: "10", action: { vm.start(minutes: 10) }, isActive: vm.isActive)
                    CircleButton(label: "20", action: { vm.start(minutes: 20) }, isActive: vm.isActive)
                    CircleButton(label: "30", action: { vm.start(minutes: 30) }, isActive: vm.isActive)
                    
                    
                }
                .frame(width: buttonSize * 3)
                
                Text("select music")
                    .font(.system(size: 35, weight: .semibold))
                    .foregroundColor(Color("textmenu"))
                    .padding(.horizontal, 40)
                    .background(Color("darkblue"))
                
                HStack(spacing: 10) {
                    Image("music1")
                        .resizable()
                        .frame(width: 90, height: 90)
                        .cornerRadius(10)
                        .onTapGesture {
                            vm.playMusic(named: "music1mp3")
                        }
                    
                    Image("music2")
                        .resizable()
                        .frame(width: 90, height: 90)
                        .cornerRadius(10)
                        .onTapGesture {
                            vm.playMusic(named: "music2mp3")
                        }

                    Image("music3")
                        .resizable()
                        .frame(width: 90, height: 90)
                        .cornerRadius(10)
                        .onTapGesture {
                            vm.playMusic(named: "music3mp3")
                        }
                    Image("music4")
                        .resizable()
                        .frame(width: 90, height: 90)
                        .cornerRadius(10)
                        .onTapGesture {
                            vm.playMusic(named: "muisc3mp3")
                        }
                }
                             
                
            }
            .onReceive(timer) { _ in
                vm.updateCountdown()
            }
        }
    }
}


struct FamilyContacts: View {
    @State private var isShowingNewContact = false
    @FetchRequest(fetchRequest: Contact.all()) private var contacts
    
    var provider = ContactsProvider.shared
    
    var body: some View {
        NavigationStack {
            List {
                ForEach(contacts) { contact in
                    ZStack(alignment: .leading) {
                        NavigationLink(destination: ContactDetailView(contact: contact)) {
                            EmptyView()
                        }
                        .opacity(0)
                        ContactRowView(contact: contact)
                    }
                }
            }
            .toolbar {
                ToolbarItem(placement: .primaryAction) {
                    Button {
                        isShowingNewContact.toggle()
                    } label: {
                        Image(systemName: "plus")
                            .font(.title)
                    }
                }
            }
            .sheet(isPresented: $isShowingNewContact) {
                NavigationStack {
                    CreateContactView(vm: .init(provider: provider))
                }
            }
            .navigationTitle("Family Contacts")
                
        }
       
    }
}


struct GroceryList: View {
        @ObservedObject var viewModel = GroceryListViewModel()
        @State private var newItemName: String = ""
        @State private var selectedEmoji: String = "🛒"
        @State private var isDropdownVisible: Bool = false
        
        var emojiOptions: [String] = ["🛒", "🍊", "🥦", "🥖", "🥚", "🥛", "🍭", "🍔", "🍗", "🍨", "🍎"]
        
        var body: some View {
            NavigationView {
                VStack {
                    List {
                        ForEach(viewModel.groceryItems) { item in
                            HStack {
                                Button(action: {
                                    viewModel.toggleGroceryItem(item)
                                }) {
                                    Image(systemName: item.isCompleted ? "checkmark.circle.fill" : "circle")
                                        .foregroundColor(item.isCompleted ? .green : .gray)
                                }
                                
                                VStack(alignment: .leading) {
                                    Text(item.name)
                                        .strikethrough(item.isCompleted)
                                    Text(item.type)
                                        .font(.caption)
                                        .foregroundColor(.gray)
                                }
                                
                                Spacer()
                                
                                Button(action: {
                                    viewModel.removeGroceryItem(item)
                                }) {
                                    Image(systemName: "trash")
                                        .foregroundColor(.red)
                                }
                            }
                        }
                    }
                    .listStyle(PlainListStyle())
                    
                    HStack {
                        TextField("Item name", text: $newItemName)
                            .textFieldStyle(RoundedBorderTextFieldStyle())
                        
                        Button(action: {
                            isDropdownVisible.toggle()
                        }) {
                            Text(selectedEmoji)
                                .font(.largeTitle)
                        }
                        .popover(isPresented: $isDropdownVisible, arrowEdge: .bottom) {
                            Picker(selection: $selectedEmoji, label: Text("")) {
                                ForEach(emojiOptions, id: \.self) { emoji in
                                    Text(emoji)
                                        .tag(emoji)
                                }
                            }
                            .pickerStyle(InlinePickerStyle())
                            .frame(width: 200)
                        }
                        
                        Button(action: {
                            viewModel.addGroceryItem(name: newItemName, type: selectedEmoji)
                            newItemName = ""
                            selectedEmoji = "🛒"
                        }) {
                            Text("Add")
                        }
                    }
                    .padding()
                }
                .navigationTitle("Grocery List")
            }
        }
    }

struct GroceryItem: Identifiable {
    let id = UUID()
    var name: String
    var type: String
    var isCompleted: Bool = false
}

class GroceryListViewModel: ObservableObject {
    @Published var groceryItems: [GroceryItem] = []
    
    func addGroceryItem(name: String, type: String) {
        let newItem = GroceryItem(name: name, type: type)
        groceryItems.append(newItem)
    }
    
    func toggleGroceryItem(_ item: GroceryItem) {
        if let index = groceryItems.firstIndex(where: { $0.id == item.id }) {
            groceryItems[index].isCompleted.toggle()
        }
    }
    
    func removeGroceryItem(_ item: GroceryItem) {
        if let index = groceryItems.firstIndex(where: { $0.id == item.id }) {
            groceryItems.remove(at: index)
        }
    }
}

struct Appointments: View {
    
    @EnvironmentObject var myEvents: EventStore
    var body: some View {
        TabView{
            EventsListView()
                .tabItem {
                    Label("List", systemImage: "list.triangle")
                }
            EventsCalendarView()
                .tabItem {
                    Label("Calendar", systemImage: "calendar")
                    
                }
        }
    }
}

struct CircleButton: View {
    let label: String
    let action: () -> Void
    let isActive: Bool
    
    private let buttonSize: CGFloat = 80
    
    var body: some View {
        Button(action: action) {
            Text(label)
                .font(.system(size: 24, weight: .semibold))
                .foregroundColor(Color("textmenu"))
                .frame(width: buttonSize, height: buttonSize)
                .background(Color("darkblue"))
                .clipShape(Circle())
                .opacity(isActive ? 0.7 : 1.0)
        }
        .disabled(isActive)
    }
}


private let itemFormatter: DateFormatter = {
    let formatter = DateFormatter()
    formatter.dateStyle = .short
    formatter.timeStyle = .medium
    return formatter
}()



struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .environment(\.managedObjectContext, PersistenceController.preview.container.viewContext)
        
    }
}
