class ViewController: UIViewController {
    @IBOutlet weak var tableView: UITableView!
    @IBOutlet var editButton: UIBarButtonItem!
    var doneButton: UIBarButtonItem?
    var tasks = [Task]()  {
        didSet { 
            self.saveTasks()
        }
    }// Task 배열 생성
