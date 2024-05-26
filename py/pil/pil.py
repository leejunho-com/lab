import os
from PIL import Image, ImageCms

class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)

    def remove_gps_info(self):
        if input("GPS 정보를 삭제하시겠습니까? (y/n)") == 'y':
            if 'exif' in self.image.info:
                exif_dict = Image._getexif(self.image)
                if 34853 in exif_dict:  # "34853" is a pointer to the GPS information IFD
                    del exif_dict[34853]
                self.image.info['exif'] = Image._makeexif(exif_dict)

    def remove_all_exif_data(self):
        if input("모든 EXIF 데이터를 삭제하시겠습니까? (y/n)") == 'y':
            self.image.info.pop('exif', None)

    def assign_srgb_profile(self):
        icc_profile = self.image.info.get("icc_profile")
        if icc_profile is None:
            if input("ICC 프로필이 없습니다. sRGB 프로필을 할당하시겠습니까? (y/n)") == 'y':
                srgb_profile = ImageCms.createProfile("sRGB")
                self.image.info["icc_profile"] = ImageCms.ImageCmsProfile(srgb_profile).tobytes()

    def save_image(self):
        quality = int(input("저장할 이미지의 품질을 1-100 사이로 입력하세요: "))
        self.image.save(self.image_path, 'JPEG', quality=quality)

image_path = input("이미지 파일 경로를 입력하세요: ")
processor = ImageProcessor(image_path)
processor.remove_gps_info()
processor.remove_all_exif_data()
processor.assign_srgb_profile()
processor.save_image()