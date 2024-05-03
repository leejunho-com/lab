import os
import datetime
import shutil

def main():
    # 코드가 실행될 폴더의 경로를 입력 받습니다.
    target_folder = input("코드를 실행할 폴더의 경로를 입력하세요: ")
    os.chdir(target_folder)  # 코드가 실행될 폴더로 이동

    while True:
        print("분기점에 도달했습니다.")
        choice = input("다음 중 하나를 입력하세요:\n'0' 또는 'cp' 또는 'c': 복사할 세션으로 이동\n'1' 또는 'touch' 또는 't' 또는 'gen': 생성할 세션으로 이동\n'x' 또는 'exit' 또는 'q' 또는 'd': 코드 종료\n")

        if choice in ['0', 'cp', 'c']:
            target_folder_to_copy = input("복사할 폴더의 경로를 입력하세요: ")
            copy_session(target_folder_to_copy)
        elif choice in ['1', 'touch', 't', 'gen']:
            generate_session()
        elif choice in ['x', 'exit', 'q', 'd']:
            print("코드를 종료합니다.")
            break
        else:
            print("올바른 선택이 아닙니다. 다시 시도하세요.")

def copy_session(target_folder_to_copy):
    current_time = datetime.datetime.now()
    folder_name = current_time.strftime(f"egf_%Y-%m-%d_%H-%M-%S")  # 폴더명 생성

    try:
        # 폴더를 생성합니다.
        os.makedirs(folder_name)
        # 모든 하위 디렉토리명과 파일명을 가져와 더미 파일을 생성합니다.
        for root, dirs, files in os.walk(target_folder_to_copy):
            for file_name in files:
                relative_path = os.path.relpath(root, target_folder_to_copy)  # 상대 경로
                dummy_folder = os.path.join(folder_name, relative_path)
                os.makedirs(dummy_folder, exist_ok=True)  # 하위 디렉토리 생성
                dummy_file_path = os.path.join(dummy_folder, file_name)
                with open(dummy_file_path, 'w'):
                    pass  # 더미 파일 생성

        print(f"폴더와 파일을 복사하여 '{folder_name}'로 저장하였습니다.")
    except FileNotFoundError:
        print("입력한 경로에 폴더가 존재하지 않습니다. 다시 시도하세요.")
    except FileExistsError:
        print(f"'{folder_name}' 폴더가 이미 존재합니다. 다른 경로를 입력하세요.")
    
    # 추가 옵션을 선택합니다.
    choice = input("분기점으로 돌아가시겠습니까? (y/n): ")
    if choice.lower() in ['y', 'yes', 'r', 'return']:
        return
    else:
        print("코드를 종료합니다.")
        exit()

def generate_session():
    # 현재 시간을 기반으로 폴더명 생성
    current_time = datetime.datetime.now()
    folder_name = current_time.strftime("egf_%Y-%m-%d_%H-%M-%S")

    # 사용자로부터 파일 목록을 입력 받습니다.
    print("파일을 생성할 폴더에 대한 파일 목록을 입력하세요. (여러 줄에 걸쳐 입력하세요. 입력이 끝나면 빈 줄을 입력하세요.)")
    while True:
        file_or_folder_name = input("파일명 또는 폴더명을 입력하세요: ")
        if not file_or_folder_name:  # 빈 줄이 입력되면 입력을 종료합니다.
            break
        if os.path.splitext(file_or_folder_name)[1]:  # 파일 확장자가 있는 경우
            # 파일인 경우 더미 파일 생성
            file_path = os.path.join(folder_name, file_or_folder_name)
            with open(file_path, 'w'):
                pass  # 더미 파일 생성
        else:
            # 폴더인 경우 빈 폴더 생성
            folder_path = os.path.join(folder_name, file_or_folder_name)
            os.makedirs(folder_path, exist_ok=True)
    
    print(f"폴더 '{folder_name}'와 파일들이 생성되었습니다.")
    
    # 추가 옵션을 선택합니다.
    choice = input("분기점으로 돌아가시겠습니까? (y/n): ")
    if choice.lower() in ['y', 'yes', 'r', 'return']:
        return
    else:
        print("코드를 종료합니다.")
        exit()

if __name__ == "__main__":
    main()
