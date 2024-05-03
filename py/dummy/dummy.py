import os
import datetime

def create_dummy_files(target_folder):
    # 현재 시간을 가져와서 문자열로 변환합니다.
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    # 타겟 폴더의 이름을 가져옵니다.
    target_folder_name = os.path.basename(target_folder)

    # 더미 파일을 저장할 폴더의 이름을 생성합니다.
    dummy_folder_name = f"{target_folder_name}-dummy-{current_time}" #

    # 원본 폴더와 같은 경로에 더미 폴더를 생성합니다.
    dummy_folder_path = os.path.join(os.path.dirname(target_folder), dummy_folder_name) # os.path.dirname 이 함수는 파일이나 디렉토리의 상위 디렉토리
    os.makedirs(dummy_folder_path, exist_ok=True)

   # os.walk() 함수는 하위 디렉토리를 포함한 모든 파일을 순회합니다.
    for root, dirs, files in os.walk(target_folder):
        for file_name in files:
            # 원본 파일의 경로를 생성합니다.
            original_file_path = os.path.join(root, file_name)

            # 원본 파일의 경로를 생성합니다.
            relative_path = os.path.relpath(root, target_folder)
            dummy_file_path = os.path.join(dummy_folder_path, relative_path, file_name)

            # 더미 파일이 저장될 디렉토리를 생성합니다.
            os.makedirs(os.path.dirname(dummy_file_path), exist_ok=True)

            # 더미 파일을 생성합니다.
            open(dummy_file_path, 'w').close()

if __name__ == "__main__":
    # 폴더의 경로를 입력받습니다.
    target_folder = input("폴더의 경로를 입력하세요: ")
    
    # create_dummy_files 함수를 호출하여 더미 파일을 생성합니다.
    create_dummy_files(target_folder)
    
    print("더미 파일이 성공적으로 생성되었습니다.")