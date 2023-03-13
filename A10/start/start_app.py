from src.repository.activity_repo import Activity_Repo
from src.repository.file_activity_repo import ActivityTextFileRepo, ActivityBinaryFileRepo
from src.repository.file_person_repo import PersonTextFileRepo, PersonBinaryFileRepo
from src.repository.person_repo import Person_Repo
from src.services.activity_service import ActivityServices
from src.services.person_service import PersonServices
from src.services.undo_redo_service import UndoRedoService
from src.test.test_activity import Test_Activity
from src.test.test_person import Test_Person
from src.ui.UI import UI

def load_properties():
    properties = {}
    with open('../configs/settings.properties', 'r') as f:
        for line in f.readlines():
            var1, var2 = line.strip().split('=')
            var1.strip()
            var2.strip()
            properties[var1] = var2
    return properties

def start_menu():
    properties = load_properties()
    if properties['repository_type'] == 'inmemory':
        person_repository = Person_Repo()
        activity_repository = Activity_Repo()
        person_repository.generate_people()
        activity_repository.generate_activities()
    elif properties['repository_type'] == 'textfiles':
        person_repository = PersonTextFileRepo(properties['person_file'])
        activity_repository = ActivityTextFileRepo(properties['activity_file'])
    elif properties['repository_type'] == 'binaryfiles':
        person_repository = PersonBinaryFileRepo(properties['person_file_bin'])
        activity_repository = ActivityBinaryFileRepo(properties['activity_file_bin'])

    undo_service = UndoRedoService()  # redo = UndoRedoService()

    # person_repository = PersonBinaryFileRepo() #person_repository.generate_people()  (in memory)

    # person_service = PersonServices(person_repository, undo_service)
    # if a person_id is deleted -> so the person_id from the activity list --> we need activity_service

    activity_service = ActivityServices(activity_repository, undo_service)
    person_service = PersonServices(person_repository, undo_service, activity_repository)
    Test_Person()
    Test_Activity()

    start_ui = UI(person_service, activity_service, undo_service)
    start_ui.start()


start_menu()
