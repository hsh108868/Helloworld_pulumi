class ViewController: UIViewController {
    @IBOutlet weak var tableView: UITableView!
    @IBOutlet var editButton: UIBarButtonItem!
    var doneButton: UIBarButtonItem?
    var tasks = [Task]()  {
        didSet { // 프로퍼티 옵저버, tasks 배열에 할일이 추가될 때마다 유저 디폴트에 할일이 저장됨
            self.saveTasks()
        }
    }// Task 배열 생성
