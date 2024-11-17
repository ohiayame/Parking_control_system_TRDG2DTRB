import os

# 폴더 경로 설정
folder_path = r"C:/Users/USER/Parking_control_system/numberdata/CarNumberOCR"

# 폴더 내 파일을 순차적으로 접근
for index, filename in enumerate(os.listdir(folder_path)):
    # 파일이 png 형식인지 확인 123_000.jpg
    # if filename.endswith('.jpg'):
	    # front_part = filename.split('_')[0] # _의 0부분 -> 123
	    # end_part = filename.split('_')[1]# _의 1부분 (변경하지 않을 부분) -> 000

      # 새로 정리된 숫자 부분 (예: 00001, 00002 등)
	    # new_number = str(index + 1).zfill(5)  # 5자리로 맞춤

      # 새로운 파일명 생성
        new_filename = f"{filename}.jpg"
            # new_filename = f"{front_part}_{new_number}.jpg"
        if new_filename != filename:
            # 파일 경로 변경
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

print("파일 이름 정리가 완료되었습니다.")