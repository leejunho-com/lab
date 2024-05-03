import os
import re
import shutil

def organize_files(source_dir):
    # 소스 디렉토리 안의 파일 목록을 가져옵니다.
    files = os.listdir(source_dir)

    # 중복된 파일명을 저장할 리스트를 생성합니다.
    duplicate_files = []

    # 파일 목록을 순회하면서 처리합니다.
    for file in files:
        # 파일의 절대 경로를 만듭니다.
        file_path = os.path.join(source_dir, file)

        # 파일 이름에서 아티스트 이름을 추출합니다.
        match = re.search(r'\[(.*?)\]', file)
        if match:
            artist = match.group(1)
            # 아티스트 이름으로 폴더를 만듭니다.
            artist_dir = os.path.join(source_dir, artist)
            if not os.path.exists(artist_dir):
                os.makedirs(artist_dir)
            # 대상 경로를 생성합니다.
            target_path = os.path.join(artist_dir, file)
            # 대상 경로에 이미 같은 이름의 파일이 있는지 확인합니다.
            if os.path.exists(target_path):
                # 중복된 파일명을 리스트에 추가합니다.
                duplicate_files.append(file)
            else:
                # 파일을 해당 아티스트의 폴더로 이동합니다.
                shutil.move(file_path, artist_dir)

    # 중복된 파일명을 오름차순으로 정렬하고 출력합니다.
    duplicate_files.sort()
    for file in duplicate_files:
        print(f"중복된 파일명: {file}")

if __name__ == "__main__":
    # 폴더의 경로를 입력받습니다.
    source_dir = input("폴더의 경로를 입력하세요: ")
    
    # organize_files 함수를 호출하여 파일을 정리합니다.
    organize_files(source_dir)
    
    print("파일이 성공적으로 정리되었습니다.")