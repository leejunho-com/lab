import os
from PIL import Image, ImageCms

# 사용자로부터 이미지 파일 경로 입력 받기
image_path = input("Enter the path of the image file: ")

# 이미지 파일 열기
img = Image.open(image_path)

# 이미지를 RGB 모드로 변환
img = img.convert('RGB')

# 컬러 프로파일 확인
if 'icc_profile' in img.info:
    icc_profile = img.info['icc_profile']
else:
    # 컬러 프로파일이 없을 경우 sRGB로 설정
    srgb_profile = ImageCms.createProfile("sRGB")
    icc_profile = ImageCms.getOpenProfile(srgb_profile).tobytes()

# 파일 이름과 확장자 분리
file_name, file_ext = os.path.splitext(image_path)

# 파일 이름에 '[pil]' 접미어 추가하고 다시 결합
compressed_image_path = f"{file_name}[pil].jpg"

# 이미지를 압축하여 저장하면서 컬러 프로파일 유지
img.save(compressed_image_path, 'JPEG', quality=85, icc_profile=icc_profile)